# -*- coding: utf-8 -*-

'''
  sample app logic
'''

# canteen logic
import models
from base import model
from canteen import Logic, bind
from canteen.util.struct import BidirectionalEnum


## Globals
fixture_key = model.Key(models.Fixtures, 'state')


class DNSRecordType(BidirectionalEnum):

  '''  '''

  A = 0x0
  AAAA = 0x1


@bind('fixtures')
class Fixtures(Logic):

  ''' fixture logic '''

  def install(self):

    ''' install fixtures if we need to '''

    if __debug__:
      # grab state
      fixture_state = models.Fixtures.get(fixture_key)

      if not fixture_state or not fixture_state.done:
        models.fixtures()
        return True
    return False


@bind('dns')
class DNS(Logic):

  ''' injected logic class '''

  def resolve(self, hostname, record=DNSRecordType.A):

    ''' simply returns what it is given. '''

    return "logic sez: %s" % message


@bind('fetch')
class Fetch(Logic):

  ''' injected logic class '''

  def resolve(self, hostname="Hello, world!", record=DNSRecordType.A):

    ''' simply returns what it is given. '''

    return "logic sez: %s" % message
