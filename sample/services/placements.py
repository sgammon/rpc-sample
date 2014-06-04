# -*- coding: utf-8 -*-

'''

  placements service

'''

# canteen
from sample.models import Placements
from sample.base import protect, rpc, remote


@remote.public('placements')
class PlacementsAPI(rpc.Service):

  ''' i manage mock placements '''

  @remote.public(Placements)
  def list(self, request):

    ''' list placements in an external provider '''
