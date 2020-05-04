from datetime import datetime, timezone
from flask import escape, Flask, jsonify, redirect, render_template, request
import json
import os
import random
import string
import threading
import webbrowser

from Empiric.PageAccessCode import pageAccessCode
from Empiric.PageFinal import pageFinal

def unjsonify(j):
  return json.loads(j)

app = Flask(__name__, static_folder='./../static')

class StepNeedsToBeRun(Exception):
  def __init__(self, step, page):
    self._step = step
    self._page = page
  def step(self):
    return self._step
  def page(self):
    return self._page

class ManuscriptMemory():
  _pathFiles = 'collected-data/'
  _pathActive = 'active-data/'
  def __init__(self, accessCode):
    self._accessCode = accessCode
    self._stepCounter = 0
    self._stepMemory = {}
    self._time = datetime.now(tz=timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z').replace(':', '-')
  def accessCode(self):
    return self._accessCode
  def isDefaultAccessCode(self):
    return self._accessCode == AccessCodes.defaultAccessCode()
  def _filepath(self):
    if not os.path.exists(self._pathFiles):
      os.makedirs(self._pathFiles)
    tmp = self._time if self.isDefaultAccessCode() else self._accessCode
    return os.path.join(self._pathFiles, f'experiment-{tmp}.json')
  def _stepInMemory(self, step):
    return str(step) in self._stepMemory
  def _initMemory(self, step):
    self._stepMemory[str(step)] = {}
  def __getMemoryWithoutKey(self, step):
    return self._stepMemory[str(step)] if self._stepInMemory(step) else None
  def _getMemory(self, step, key):
    m = self.__getMemoryWithoutKey(step)
    return m[key] if key in m else None
  def _setMemory(self, step, key, value=None, defaultValue=None):
    m = self.__getMemoryWithoutKey(step)
    if key in m:
      if value is not None:
        m[key] = value
    else:
      m[key] = value if value is not None else defaultValue
  def prepareRun(self):
    self._stepCounter = 0
    if not self.isDefaultAccessCode() and self._stepMemory == {}:
      if os.path.exists(self._filepath()):
        with open(self._filepath(), 'r') as f:
          self._stepMemory = json.load(f)['log']
  def runStep(self, page):
    self._stepCounter += 1
    if not self._stepInMemory(self._stepCounter):
      self._initMemory(self._stepCounter)
    self._setMemory(self._stepCounter, 'typeOfPage', defaultValue=page.__class__.__name__)
    self._setMemory(self._stepCounter, 'settings', defaultValue=page.settings())
    result = self._getMemory(self._stepCounter, 'result')
    if result:
      return result
    raise StepNeedsToBeRun(self._stepCounter, page)
  def save(self, step, result):
    if not step or not self._stepInMemory(step) or self._getMemory(step, 'result') is not None:
      return None
    result['timestamp'] = datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    self._setMemory(step, 'result', defaultValue=result)
    with open(self._filepath(), 'w') as f:
      json.dump({'log': self._stepMemory}, f)
    return result
  def settings(self, step):
    settings = self._getMemory(step, 'settings')
    return settings if settings is not None else {}

class ManuscriptMemories():
  def __init__(self):
    self._ms = {}
  def get(self, accessCode):
    if accessCode not in self._ms:
      self._ms[accessCode] = ManuscriptMemory(accessCode)
    return self._ms[accessCode]

class AccessCodes():
  _accessCodeLength = 8
  _fileAccessCodes = 'access-codes.csv'
  _defaultAccessCode = '_'
  def __init__(self, useAccessCodes, numberOfAccessCodes):
    self._accessCodes = []
    if not useAccessCodes:
      self._accessCodes = [self._defaultAccessCode]
    else:
      self._accessCodes = None
      if os.path.exists(self._fileAccessCodes):
        print(' * Load list of access codes')
        with open(self._fileAccessCodes, 'r') as f:
          self._accessCodes = f.read().splitlines()
      if self._accessCodes is None or len(self._accessCodes) < numberOfAccessCodes:
        print(' * Generate list of access codes' if self._accessCodes is None else ' * Extend list of access codes')
        if self._accessCodes is None:
          self._accessCodes = []
        while len(self._accessCodes) < numberOfAccessCodes:
          accessCode = ''.join(random.choice(string.ascii_letters) for _ in range(0, self._accessCodeLength))
          if accessCode not in self._accessCodes:
            self._accessCodes.append(accessCode)
        with open(self._fileAccessCodes, 'w') as f:
          f.write('\n'.join(self._accessCodes))
  def exists(self, accessCode):
    return accessCode in self._accessCodes
  @staticmethod
  def defaultAccessCode():
    return AccessCodes._defaultAccessCode

class Experiment:
  def __init__(self, port=5000, debug=False, openBrowser=True):
    self._port = port
    self._debug = debug
    self._openBrowser = openBrowser
    self._ms = ManuscriptMemories()
  def run(self, manuscript, useAccessCodes=False, numberOfAccessCodes=1000):
    self._ac = AccessCodes(useAccessCodes, numberOfAccessCodes)
    @app.route('/')
    def base():
      if useAccessCodes:
        return pageAccessCode(None)
      else:
        return redirect('/' + AccessCodes.defaultAccessCode())
    @app.route('/<string:accessCode>')
    def step(accessCode):
      if not self._ac.exists(accessCode):
        return pageAccessCode(None, showErrorMessage=True)
      m = self._ms.get(accessCode)
      m.prepareRun()
      try:
        manuscript(m)
        pageFinal(m)
      except StepNeedsToBeRun as e:
        return render_template(e.page().template(), accessCode=m.accessCode(), step=e.step())
    @app.route('/save/<string:accessCode>/<int:step>', methods=['POST'])
    def save(accessCode, step):
      if not self._ac.exists(accessCode):
        return jsonify({'success': False})
      self._ms.get(accessCode).save(step, request.get_json())
      return jsonify({'success': True})
    @app.route('/settings/<string:accessCode>/<int:step>')
    def settings(accessCode, step):
      if not self._ac.exists(accessCode):
        return jsonify({'success': False})
      return jsonify(self._ms.get(accessCode).settings(step))
    if self._openBrowser:
      threading.Timer(1, lambda: webbrowser.open(f'http://127.0.0.1:{self._port}')).start()
    app.run(port=self._port, debug=self._debug)
