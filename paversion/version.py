

class Version(object):
  def __init__(self, major = 0, minor = 0, patch = 0):
    self.major = major
    self.minor = minor
    self.patch = patch

  def bump_major(self):
    self.major += 1
    self.minor = 0
    self.patch = 0
    return self

  def bump_minor(self):
    self.minor += 1
    self.patch = 0
    return self

  def bump_patch(self):
    self.patch += 1
    return self

  def __repr__(self):
    return "Version(%i, %i, %i)" % (self.major, self.minor, self.patch)


