from datetime import datetime, timezone
from flask import escape, Flask, jsonify, render_template, request
import json
import os
import threading
import webbrowser

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
  _stepCounter = 0
  _stepMemory = {}
  _time = datetime.now(tz=timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z').replace(':', '-')
  _pathFiles = 'collected-data/'
  def prepareRun(self):
    self._stepCounter = 0
  def runStep(self, page):
    self._stepCounter += 1
    if self._stepCounter not in self._stepMemory:
      self._stepMemory[self._stepCounter] = {}
    if 'typeOfPage' not in self._stepMemory[self._stepCounter]:
      self._stepMemory[self._stepCounter]['typeOfPage'] = page.__class__.__name__
    if 'settings' not in self._stepMemory[self._stepCounter]:
      self._stepMemory[self._stepCounter]['settings'] = page.settings()
    if self._stepCounter in self._stepMemory and 'result' in self._stepMemory[self._stepCounter]:
      return self._stepMemory[self._stepCounter]['result']
    raise StepNeedsToBeRun(self._stepCounter, page)
  def save(self, step, result):
    if not step or step not in self._stepMemory or 'result' in self._stepMemory[step]:
      return None
    result['timestamp'] = datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    self._stepMemory[step]['result'] = result
    if not os.path.exists(self._pathFiles):
      os.makedirs(self._pathFiles)
    with open(os.path.join(self._pathFiles, f'experiment-{self._time}.json'), 'w') as f:
      json.dump(self._stepMemory, f)
    return result
  def settings(self, step):
    if not step or step not in self._stepMemory or 'settings' not in self._stepMemory[step]:
      return {}
    return self._stepMemory[step]['settings']

class Experiment:
  def __init__(self, port=5000, debug=False, openBrowser=True):
    self._port = port
    self._debug = debug
    self._openBrowser = openBrowser
    self._m = ManuscriptMemory()
  def run(self, manuscript):
    @app.route('/')
    def step():
      self._m.prepareRun()
      try:
        manuscript(self._m)
        pageFinal(self._m)
      except StepNeedsToBeRun as e:
        return render_template(e.page().template(), step=e.step())
    
    @app.route('/save/<int:step>', methods=['POST'])
    def save(step):
      self._m.save(step, request.get_json())
      return jsonify({'success': True})

    @app.route('/settings/<int:step>')
    def settings(step):
      return jsonify(self._m.settings(step))
    
    if self._openBrowser:
      threading.Timer(1, lambda: webbrowser.open(f'http://127.0.0.1:{self._port}')).start()
    
    app.run(port=self._port, debug=self._debug)
