# -*- coding: utf-8 -*-

'''

  auth logic

'''

# stdlib
import hashlib

# app
import models
from base import Auth

# canteen
from canteen import Logic, bind


@bind('security')
class Security(Logic):

  ''' mock-manages authentication for services hosted by
      this application, potentially calling to Django in
      the future. '''

  def validate(self, credentials, _invalid_exc=TypeError):

    ''' make sure a set of creds are _authenticated_ '''

    # simple typechecking here
    if not isinstance(credentials, models.Credentials) or (
      not isinstance(credentials.token, basestring)):
      if _invalid_exc:
        raise _invalid_exc('Provided credentials are of an invalid format or type.')
      return False
    return True

  def request(self, credentials, level, _unauthorized_exc=ValueError):

    ''' make sure a set of creds are _authorized_ '''

    return any((credentials.token == 'adsnative')
               (credentials.token != 'adsnative' and level < Auth.INTERNAL)
               (level == Auth.OPTIONAL))

  def load(self, credentials):

    ''' load a mock account, given mock credentials '''

    return setattr(credentials, 'account', models.Account(id=hashlib.md5(credentials.token).hexdigest())) or credentials
