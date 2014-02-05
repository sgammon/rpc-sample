# -*- coding: utf-8 -*-

'''
  sample app logic
'''

# canteen logic
from canteen import Logic, decorators


@decorators.bind('hello')
class GenerateHello(Logic):

  ''' injected logic class '''

  def say_hello(self, message="Hello, world!"):

    ''' simply returns what it is given. '''

    return "logic sez: %s" % message
