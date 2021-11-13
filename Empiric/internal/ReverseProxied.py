class ReverseProxied(object):
  def __init__(self, app, scriptName=None, scheme=None, server=None):
    self.app = app
    self.scriptName = scriptName
    self.scheme = scheme
    self.server = server

  def __call__(self, environ, start_response):
    scriptName = environ.get('HTTP_X_SCRIPT_NAME', '') or self.scriptName
    if scriptName:
      environ['SCRIPT_NAME'] = scriptName
      pathInfo = environ['PATH_INFO']
      if pathInfo.startswith(scriptName):
        environ['PATH_INFO'] = pathInfo[len(scriptName):]
    scheme = environ.get('HTTP_X_SCHEME', '') or self.scheme
    if scheme:
      environ['wsgi.url_scheme'] = scheme
    server = environ.get('HTTP_X_FORWARDED_SERVER', '') or self.server
    if server:
      environ['HTTP_HOST'] = server
    return self.app(environ, start_response)
