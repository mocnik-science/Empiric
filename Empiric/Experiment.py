from flask import Flask, jsonify, redirect, render_template, request
import os
import shutil
import sys
import subprocess
import threading
import webbrowser

from Empiric import pkgName, pkgVersion, pkgUrl
from Empiric.internal.AccessCodes import AccessCodes
from Empiric.internal.ManuscriptMemory import ManuscriptMemories, StepNeedsToBeRun
from Empiric.internal.Print import COLORS
from Empiric.PageAccessCode import pageAccessCode
from Empiric.PageFinal import pageFinal

class Experiment:
  _pathStaticFile = 'files'
  def __init__(self):
    self._ms = ManuscriptMemories()
    self._info()
  def _log(self, *msgs):
    msg = ''.join(msgs)
    print(f' * {msg}')
  def _log2(self, *msgs):
    msg = ''.join(msgs)
    print(f'   {msg}')
  def _info(self):
    width = 54
    self._log2()
    self._log2('=' * width)
    self._log2('== ', f'{pkgName} v{pkgVersion}', ' ' * (width - 8 - len(pkgName) - len(pkgVersion)), ' ==')
    self._log2('== ', pkgUrl, ' ' * (width - 6 - len(pkgUrl)), ' ==')
    self._log2('=' * width)
    self._log2()
  def _yarnCheck(self):
    try:
      self._log('Checking for Yarn')
      subprocess.run(['yarn', '--version'], capture_output=True)
      self._log2('Found')
    except:
      self._log2()
      self._log2(f'{COLORS.ERROR}ERROR: Yarn is needed. Please install it.')
      self._log2()
      self._log2('You find Yarn here:  https://yarnpkg.com')
      self._log2()
      self._log2('Yarn is required to download libraries needed for the')
      self._log2(f'web interface.{COLORS.DEFAULT}')
      self._log2()
      return False
    return True
  def _yarnCopyPackageFiles(self, pathStatic):
    try:
      if not os.path.exists(pathStatic):
        self._log('Creating path for static data')
        os.makedirs(pathStatic)
        self._log2('Success')
      self._log('Copy files to the path for static data')
      for filename in ['package.json', '.yarnrc']:
        shutil.copy(os.path.join(os.path.dirname(__file__), '..', 'files', filename), os.path.join(pathStatic, filename))
      self._log2('Success')
    except:
      self._log2()
      self._log2(f'{COLORS.ERROR}ERROR: Could not copy Yarn package files.{COLORS.DEFAULT}')
      self._log2()
      return False
    return True
  def _yarnInstall(self, pathStatic):
    try:
      self._log('Installing JavaScript libraries using yarn')
      subprocess.run(['yarn', 'install'], capture_output=True, cwd=pathStatic)
      self._log2('Success')
    except:
      self._log2()
      self._log2(f'{COLORS.ERROR}ERROR: Yarn could not install the libraries needed.')
      self._log2()
      self._log2('Please run yarn on your own:')
      self._log2(f'> cd static && yarn install{COLORS.DEFAULT}')
      self._log2()
      return False
    return True
  def _createPathStaticFile(self, pathStatic):
    try:
      p = os.path.join(pathStatic, Experiment._pathStaticFile)
      if not os.path.exists(p):
        self._log('Creating path for static files')
        os.makedirs(p)
        self._log2('Success')
    except:
      self._log2()
      self._log2(f'{COLORS.ERROR}ERROR: Could not create path for static files.{COLORS.DEFAULT}')
      self._log2()
      return False
    return True
  def run(self, manuscript, port=5000, debug=False, openBrowser=True, pathStatic=None, useAccessCodes=False, numberOfAccessCodes=1000):
    self._port = port
    self._debug = debug
    self._openBrowser = openBrowser
    self._pathStatic = pathStatic if pathStatic else os.path.join(os.path.dirname(sys.argv[0]), 'static')
    self._readyToStart = self._yarnCheck() and self._yarnCopyPackageFiles(self._pathStatic) and self._yarnInstall(self._pathStatic) and self._createPathStaticFile(self._pathStatic)
    if not self._readyToStart:
      return
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
