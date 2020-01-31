class Page():
  def __init__(self, m, template):
    self._m = m
    self._template = template
  def run(self, **settings):
    self._settings = settings
    return self._m.runStep(self)
  def template(self):
    return self._template
  def settings(self):
    return self._settings
