# -*- coding: utf-8 -*-

'''
  sample canteen app yay!
'''

# stdlib
import pdb

# sample app
from sample import models

# canteen
from canteen import url, Page
if __debug__: from canteen.model.adapter import inmemory


# homepage!
@url('home', u'/')
class Homepage(Page):

  '''  '''

  if __debug__:

    # bind metadata/datastore for introspection
    __metadata__, __datastore__, metadata, datastore = (
      inmemory._metadata,
      inmemory._datastore,
      property(lambda self: self.__metadata__),
      property(lambda self: self.__datastore__)
    )

  def GET(self):

    ''' handles HTTP GET '''

    # allow interactive breakpoints for inspection
    if __debug__ and self.request.args.get('debug'): pdb.set_trace()

    # make sure fixtures are installed
    self.fixtures.install()

    return self.render('home.haml', message='hi')
