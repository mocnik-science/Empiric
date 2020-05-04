from flask import render_template

class Page():
  def __init__(self, m, template):
    self._m = m
    self._template = template
  def run(self, **settings):
    self._settings = settings
    return self._m.runStep(self) if self._m is not None else None
  def render(self, **settings):
    return render_template(self.template(), step=-1, **settings)
  def template(self):
    return self._template
  def settings(self):
    return self._settings
