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
  @staticmethod
  def _camelCase(s):
    s = ''.join([c for c in s.replace('-', ' ') if c.isalnum() or c == ' '])
    return ''.join(x.capitalize() for x in s.split(' '))
  def _filepath(self):
    if not os.path.exists(self._pathCollectedData):
      os.makedirs(self._pathCollectedData)
    return os.path.join(GeneralSettings._pathCollectedData, GeneralSettings._generalSettings)
  @staticmethod
  def fixKeyTitle(statistics):
    if 'key' not in statistics and 'title' in statistics:
      statistics['key'] = GeneralSettings._camelCase(statistics['title'])
    if 'title' not in statistics and 'key' in statistics:
      statistics['title'] = statistics['key']
    return statistics
  def get(self, key=None):
    if key is None:
      return self._generalSettings
    else:
      return self._generalSettings[key] if key in self._generalSettings else None
  def setStatistics(self, statistics):
    statistics = GeneralSettings.fixKeyTitle(statistics)
    if 'key' in statistics:
      if statistics['key'] not in self._generalSettings['statistics']:
        self._generalSettings['statistics'][statistics['key']] = statistics
      return statistics['key']
    return None
  def save(self):
    with open(self._filepath(), 'w') as f:
      json.dump(self._generalSettings, f)
    return self._generalSettings
