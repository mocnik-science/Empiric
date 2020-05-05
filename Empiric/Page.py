from flask import render_template

class Page():
  def __init__(self, m, template):
    self._m = m
    self._template = template
    self._settings = None
    self._statistics = None
  def _storeSettings(self, **kwargs):
    self._statistics = None
    if 'statistics' in kwargs:
      self._statistics = kwargs['statistics']
      del kwargs['statistics']
    self._settings = kwargs
  def run(self, **kwargs):
    self._storeSettings(**kwargs)
    return self._m.runStep(self) if self._m is not None else None
  def render(self, **kwargs):
    self._storeSettings(**kwargs)
    return render_template(self.template(), step=-1, **self.settings())
  def template(self):
    return self._template
  def settings(self):
    return self._settings
  def statistics(self):
    return self._statistics
