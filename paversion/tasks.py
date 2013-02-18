
import os
from paver.tasks import task, environment

VERSION_FILE = os.path.abspath(os.path.join(environment.pavement_file, "..", ".version"))

@task
def bump_patch():
  print VERSION_FILE


@task
def bump_minor():
  pass


@task
def bump_major():
  pass