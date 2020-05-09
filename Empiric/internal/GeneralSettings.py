import json
import os

class GeneralSettings():
  _pathCollectedData = 'collected-data/'
  _generalSettings = 'settings.json'
  def __init__(self):
    if not os.path.exists(GeneralSettings._pathCollectedData):
      os.makedirs(GeneralSettings._pathCollectedData)
    if os.path.exists(self._filepath()):
      with open(self._filepath(), 'r') as f:
        self._generalSettings = json.load(f)
    else:
      self._generalSettings = {
        'statistics': {},
      }
  def _filepath(self):
    if not os.path.exists(self._pathCollectedData):
      os.makedirs(self._pathCollectedData)
    return os.path.join(GeneralSettings._pathCollectedData, GeneralSettings._generalSettings)
  def get(self):
    return self._generalSettings
  def saveStatistics(self, statistics):
    self._generalSettings['statistics'] = statistics
  def save(self):
    with open(self._filepath(), 'w') as f:
      json.dump(self._generalSettings, f)
    return self._generalSettings
