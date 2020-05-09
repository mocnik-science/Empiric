class Step():
  def __init__(self, m):
    self._m = m
    self._settings = None
    self._statistics = None
  def _storeSettings(self, statistics=None, **kwargs):
    self._settings = kwargs
    if 'defaultStatistics' in kwargs:
      if isinstance(statistics, str):
        self._statistics = kwargs['defaultStatistics']
        self._statistics['title'] = statistics
      else:
        self._statistics = statistics
      del kwargs['defaultStatistics']
    else:
      self._statistics = statistics
  def run(self, raiseError=False, **kwargs):
    self._storeSettings(**kwargs)
    return self._m.runStep(self, raiseError=raiseError) if self._m is not None else None
  def save(self, result):
    return self._m.saveCurrentStep(result)
  def settings(self):
    return self._settings
  def statistics(self):
    return self._statistics
