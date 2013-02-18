import os
import sys
from   subprocess  import call
from   paver.tasks import task

# How's this for eating our own dogfood?  :-D
import paversion.tasks



class TestsFailed(Exception):
  pass


@task
def test():
  result = call([sys.executable, os.path.abspath(os.path.join(__file__, "..", "setup.py")), "test"])
  if result != 0:
    raise TestsFailed("Unit tests have failed.")

