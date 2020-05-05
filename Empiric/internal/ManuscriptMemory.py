from datetime import datetime, timezone
import json
import os

from Empiric.internal.AccessCodes import AccessCodes

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
    self._data = {
      'log': {},
    }
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
  def _logEmpty(self):
    return self._data['log'] == {}
  def _stepInLog(self, step):
    return str(step) in self._data['log']
  def _initStep(self, step):
    self._data['log'][str(step)] = {}
  def __getLogWithoutKey(self, step):
    return self._data['log'][str(step)] if self._stepInLog(step) else None
  def _getLog(self, step, key):
    m = self.__getLogWithoutKey(step)
    return m[key] if key in m else None
  def _setLog(self, step, key, value=None, defaultValue=None):
    m = self.__getLogWithoutKey(step)
    if key in m:
      if value is not None:
        m[key] = value
    else:
      m[key] = value if value is not None else defaultValue
  def prepareRun(self):
    self._stepCounter = 0
    if not self.isDefaultAccessCode() and self._logEmpty():
      if os.path.exists(self._filepath()):
        with open(self._filepath(), 'r') as f:
          self._data = json.load(f)
  def runStep(self, page):
    self._stepCounter += 1
    if not self._stepInLog(self._stepCounter):
      self._initStep(self._stepCounter)
    self._setLog(self._stepCounter, 'typeOfPage', defaultValue=page.__class__.__name__)
    self._setLog(self._stepCounter, 'settings', defaultValue=page.settings())
    result = self._getLog(self._stepCounter, 'result')
    if result:
      return result
    raise StepNeedsToBeRun(self._stepCounter, page)
  def save(self, step, result):
    if not step or not self._stepInLog(step) or self._getLog(step, 'result') is not None:
      return None
    result['timestamp'] = datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    self._setLog(step, 'result', defaultValue=result)
    with open(self._filepath(), 'w') as f:
      json.dump(self._data, f)
    return result
  def settings(self, step):
    settings = self._getLog(step, 'settings')
    return settings if settings is not None else {}

class ManuscriptMemories():
  def __init__(self):
    self._ms = {}
  def get(self, accessCode):
    if accessCode not in self._ms:
      self._ms[accessCode] = ManuscriptMemory(accessCode)
    return self._ms[accessCode]
