# -*- coding: utf-8 -*-

'''
  sample services yay!
'''

# canteen
from canteen import rpc, model
from canteen.rpc import remote


class HelloMessage(model.Model):

  ''' i hold a simple message '''

  message = basestring, {'default': 'Hello, world!'}


@remote.public('hello')
class HelloService(rpc.Service):

  ''' i say things for testing '''

  @remote.public(HelloMessage)
  def say_something(self, request):

    ''' i echo back what i am given '''

    return HelloMessage(message=self.hello.say_hello(request.message))
