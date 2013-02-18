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


  def test_bump_patch_increments_the_patch(self):
    self.assertEqual(Version(1, 2, 3).bump_patch(), Version(1, 2, 4))
  
  def test_bump_patch_returns_a_new_Version(self):
    v = Version(1, 2, 3)
    self.assertNotEqual(id(v), id(v.bump_patch()))
    self.assertEqual(v, Version(1, 2, 3))


  def test_bump_minor_increments_the_minor_and_resets_patch(self):
    self.assertEqual(Version(1, 2, 3).bump_minor(), Version(1, 3, 0))
  
  def test_bump_minor_returns_a_new_Version(self):
    v = Version(1, 2, 3)
    self.assertNotEqual(id(v), id(v.bump_minor()))
    self.assertEqual(v, Version(1, 2, 3))
  

  def test_bump_major_increments_the_major_and_resets_minor_and_patch(self):
    self.assertEqual(Version(1, 2, 3).bump_major(), Version(2, 0, 0))

  def test_bump_major_returns_a_new_Version(self):
    v = Version(1, 2, 3)
    self.assertNotEqual(id(v), id(v.bump_major()))
    self.assertEqual(v, Version(1, 2, 3))


