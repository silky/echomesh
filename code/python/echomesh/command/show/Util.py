from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.util import Log

LOGGER = Log.logger(__name__)

def indent(s, spaces='  '):
  return '\n'.join(spaces + i.strip() for i in s.split('\n'))

def info(d, spaces='  '):
  s = 'none'
  if d:
    items = [(('%s%s:' % (spaces, k)), v) for k, v in sorted(six.iteritems(d))]
    length = max(len(k) for k, v in items)
    s = '\n'.join('%-*s %s' % (length, k, v) for k, v in items)
  LOGGER.info('%s\n', s)

