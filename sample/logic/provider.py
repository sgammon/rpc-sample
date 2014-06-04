# -*- coding: utf-8 -*-

'''

  provider logic

'''

# canteen logic
from canteen import Logic, decorators


@decorators.bind('provider')
class MockProvider(Logic):

  ''' injected logic class '''

  def resolve(self):

    ''' simply returns what it is given. '''

    return "logic sez: %s" % message
