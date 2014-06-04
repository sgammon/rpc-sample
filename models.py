# -*- coding: utf-8 -*-

'''

  models

'''

# stdlib
import hashlib
import traceback

# canteen
from base import Model, model


## !! Accounting !! ##
class Account(Model):

  ''' i am a mock account '''

  id = basestring, {'required': True}


class Credentials(Model):

  ''' i am some client credentials '''

  token = basestring
  account = model.Key


## !! Placements !! ##
class Placement(Model):

  ''' i am a mock placement '''

  id = basestring, {'required': True}
  claimed = bool, {'default': False}
  owner_campaign = basestring


class Placements(Model):

  ''' i hold mock placements '''

  account = basestring, {'required': True}
  placements = Placement, {'repeated': True}


## !! Campaigns !! ##
class Campaign(Model):

  ''' i am a mock campaign '''

  id = basestring, {'required': True}


class Campaigns(Model):

  ''' i hold mock campaigns '''

  count = int, {'default': 0}
  campaigns = Campaign, {'repeated': True}


## !! Utilities !! ##
class Fixtures(Model):

  ''' i hold fixture state '''

  done = bool, {'default': True}


def fixtures():

  ''' add fixture models '''

  # resolve current base adapter
  if not isinstance(Model.__adapter__, basestring):
    adapter = Model.__adapter__.__class__.__name__
  else:
    adapter = Model.__adapter__

  # make sure we're not running in prod
  assert __debug__, "can only run fixtures in debug mode"
  assert adapter == "InMemoryAdapter", "cannot use fixtures with non-testing adapter, got %s" % str(Model.__adapter__)

  # spawn accounts
  accounts = account_a, account_b, account_c = [
    Account.factory(i) for i in ('alpha', 'bravo', 'charlie')
  ]

  # credentials (internal first)
  credentials = [
    Credentials.factory('adsnative_admin'),
    Credentials.factory(account_a, 'blab1'),
    Credentials.factory(account_b, 'blab2'),
    Credentials.factory(account_c, 'blab3')
  ]

  # placements (linked to accounts)
  placements = [Placement.factory(hashlib.md5(str(x)).hexdigest()) for x in xrange(10)]

  results, failures = [], 0
  for group in (accounts, credentials, placements):
    for _m in group:
      try:
        result = _m.put()
      except Exception as e:
        failures += 1
        traceback.print_exc()
      else:
        results.append(result)
        print "Stored fixture of type '%s' at key '%s'..." % (_m.kind(), result.urlsafe())

  # indicate that fixtures are installed
  if not failures: Fixtures(key=model.Key(Fixtures, 'state')).put()
  print "Fixtures completed and stored %s items along the way with %s failures." % (len(results), str(failures))
