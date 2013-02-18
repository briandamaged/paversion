from paversion.version import Version
from unittest import TestCase


class Test_Version(TestCase):

  def test_versions_are_equal_if_all_components_match(self):
    v1 = Version(1, 2, 3)
    v2 = Version(1, 2, 3)
    
    self.assertEqual(v1, v2)
    self.assertEqual(hash(v1), hash(v2))


  def test_versions_are_not_equal_when_patch_is_different(self):
    v1 = Version(1, 2, 3)
    v2 = Version(1, 2, 4)
    
    self.assertNotEqual(v1, v2)
    self.assertNotEqual(hash(v1), hash(v2))


  def test_versions_are_not_equal_when_minor_is_different(self):
    v1 = Version(1, 2, 3)
    v2 = Version(1, 5, 3)
    
    self.assertNotEqual(v1, v2)
    self.assertNotEqual(hash(v1), hash(v2))


  def test_versions_are_not_equal_when_major_is_different(self):
    v1 = Version(1, 2, 3)
    v2 = Version(2, 2, 3)
    
    self.assertNotEqual(v1, v2)
    self.assertNotEqual(hash(v1), hash(v2))


