# from __future__ import absolute_import, division, print_function, unicode_literals

from contextlib import closing
import os.path
import os
import platform
import socket
import sys

from echomesh.base import Platform

def ip_address():
  try:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as s:
      s.connect(('8.8.8.8', 80))
      return s.getsockname()[0]
  except:
    return '(none)'

if Platform.IS_LINUX:
  import fcntl, socket, struct

  # From here: http://stackoverflow.com/questions/159137/getting-mac-address
  def get_hw_addr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # b = b'256s'
    b = '256s'
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack(b, ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

  def mac_address():
    return get_hw_addr('eth0')

else:
  import uuid
  def mac_address():
    myMAC = uuid.getnode()
    return ':'.join('%02X' % ((myMAC >> 8*i) & 0xff) for i in reversed(xrange(6)))

MAC_ADDRESS = mac_address()
IP_ADDRESS = ip_address()
NAME = platform.uname()[1]

CODE_PATH = os.path.abspath(sys.path[0])
ECHOMESH_PATH = os.path.dirname(os.path.dirname(CODE_PATH))
PROJECT_PATH = ECHOMESH_PATH

def set_name(name):
  global NAME
  NAME = name

def _not_possible_project(path):
  for d in 'asset', 'command':
    if not os.path.exists(os.path.join(path, d)):
      return True

def set_project_path(original_path):
  path = os.path.abspath(os.path.expanduser(original_path))

  while _not_possible_project(path):
    p = os.path.dirname(path)
    if p == path:
      print("The path %s wasn't in an echomesh project " % original_path)
      return

  os.chdir(path)

  global PROJECT_PATH
  PROJECT_PATH = path

def names():
  return MAC_ADDRESS, IP_ADDRESS, NAME

