from Empiric.internal.StatisticsTools import StatisticsTools

class Step():
  def __init__(self, m):
    self._m = m
    self._settings = None
    self._metadata = self._m.metadata() if self._m is not None else {}
    self._statistics = None
  def _storeSettings(self, statistics=None, defaultStatistics=None, appendToDefaultStatistics=True, hideStatisticsByDefault=False, **kwargs):
    self._settings = kwargs
    self._statistics = StatisticsTools.mergeWithDefaultStatistics(statistics, defaultStatistics, appendToDefaultStatistics, hideStatisticsByDefault)
  def run(self, raiseError=False, **kwargs):
    self._storeSettings(**kwargs)
    return self._m.runStep(self, raiseError=raiseError) if self._m is not None else None
  def save(self, result):
    return self._m.saveCurrentStep(result)
  def settings(self):
    return self._settings
  def metadata(self):
    return self._metadata
  def statistics(self):
    return self._statistics
