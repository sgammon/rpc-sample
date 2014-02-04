# -*- coding: utf-8 -*-

'''
  sample canteen app yay!
'''

# canteen
from canteen import url, Page


# homepage!
@url('home', u'/')
class Homepage(Page):

  '''  '''

  def GET(self):

    '''  '''

    return self.render('home.haml')
