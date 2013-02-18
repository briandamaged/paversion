

class Version(object):
  """
  Simple Version class that supports versions of the form:
  
    major.minor.patch
  
  For example:
  
    0.4.2
  
  For now, I'm not going to bother with supporting any other
  version formats.  We can add them if anyone actually expresses
  an interested to do so.
  """
  def __init__(self, major = 0, minor = 0, patch = 0):
    self.__major = major
    self.__minor = minor
    self.__patch = patch
  
  @property
  def major(self):
    return self.__major

  @property
  def minor(self):
    return self.__minor

  @property
  def patch(self):
    return self.__patch


  def bump_major(self):
    return Version(self.major + 1, 0, 0)

  def bump_minor(self):
    return Version(self.major, self.minor + 1, 0)

  def bump_patch(self):
    return Version(self.major, self.minor, self.patch + 1)


  @property
  def tuple(self):
    return (self.major, self.minor, self.patch)

  def __eq__(self, rhs):
    return isinstance(rhs, Version) and self.tuple == rhs.tuple

  def __hash__(self):
    return hash((self.major, self.minor, self.patch))

  def __repr__(self):
    return "Version(%i, %i, %i)" % (self.major, self.minor, self.patch)



class VersionManager(object):
  def __init__(self):
    self.__version = None

  @property
  def version(self):
    if self.__version is None:
      self.__version = Version(0, 0, 0)

    return self.__version




