class AccessCodes():
  _accessCodeLength = 8
  _fileAccessCodes = 'access-codes.csv'
  _defaultAccessCode = '_'
  def __init__(self, useAccessCodes, numberOfAccessCodes):
    self._accessCodes = []
    if not useAccessCodes:
      self._accessCodes = [self._defaultAccessCode]
    else:
      self._accessCodes = None
      if os.path.exists(self._fileAccessCodes):
        print(' * Load list of access codes')
        with open(self._fileAccessCodes, 'r') as f:
          self._accessCodes = f.read().splitlines()
      if self._accessCodes is None or len(self._accessCodes) < numberOfAccessCodes:
        print(' * Generate list of access codes' if self._accessCodes is None else ' * Extend list of access codes')
        if self._accessCodes is None:
          self._accessCodes = []
        while len(self._accessCodes) < numberOfAccessCodes:
          accessCode = ''.join(random.choice(string.ascii_letters) for _ in range(0, self._accessCodeLength))
          if accessCode not in self._accessCodes:
            self._accessCodes.append(accessCode)
        with open(self._fileAccessCodes, 'w') as f:
          f.write('\n'.join(self._accessCodes))
  def exists(self, accessCode):
    return accessCode in self._accessCodes
  @staticmethod
  def defaultAccessCode():
    return AccessCodes._defaultAccessCode
