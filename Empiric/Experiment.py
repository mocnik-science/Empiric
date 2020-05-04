from flask import Flask, jsonify, redirect, render_template, request
import os
import sys
import threading
import webbrowser

from Empiric.internal.AccessCodes import AccessCodes
from Empiric.internal.ManuscriptMemory import ManuscriptMemories, StepNeedsToBeRun
from Empiric.PageAccessCode import pageAccessCode
from Empiric.PageFinal import pageFinal

class Experiment:
  def __init__(self):
    self._ms = ManuscriptMemories()
  def run(self, manuscript, port=5000, debug=False, openBrowser=True, pathStatic=None, useAccessCodes=False, numberOfAccessCodes=1000):
    self._port = port
    self._debug = debug
    self._openBrowser = openBrowser
    self._pathStatic = pathStatic if pathStatic else os.path.join(os.path.dirname(sys.argv[0]), 'static')
    self._ac = AccessCodes(useAccessCodes, numberOfAccessCodes)
    app = Flask(__name__, static_folder=self._pathStatic)
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
