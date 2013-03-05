from __future__ import absolute_import, division, print_function, unicode_literals

import copy
import os
import os.path
import sys

from echomesh.base import Yaml

CODE_PATH = os.path.abspath(sys.path[0])
ECHOMESH_PATH = os.path.dirname(os.path.dirname(CODE_PATH))
PROJECT_PATH = None
COMMAND_PATH = None
ASSET_PATH = None

def _possible_project(path):
  for d in 'asset', 'command':
    if not os.path.exists(os.path.join(path, d)):
      return False
  return True

def set_project_path(project_path=None, show_error=False):
  original_path = os.path.abspath(os.path.expanduser(project_path or os.curdir))
  path = original_path

  while not _possible_project(path):
    p = os.path.dirname(path)
    if p != path:
      path = p
    else:
      if show_error:
        print("\nYour path %s isn't in an echomesh project." % original_path)
        print("Defaulting to the echomesh path %s." % ECHOMESH_PATH)
      path = ECHOMESH_PATH
      break

  global PROJECT_PATH, COMMAND_PATH, ASSET_PATH
  PROJECT_PATH = path
  COMMAND_PATH = os.path.join(path, 'command')
  ASSET_PATH = os.path.join(path, 'asset')
  os.chdir(path)

set_project_path()

def info():
  return {
    'Asset path': ASSET_PATH,
    'Code path': CODE_PATH,
    'Command path': COMMAND_PATH,
    'Project path': PROJECT_PATH,
    'echomesh path': ECHOMESH_PATH,
    }
