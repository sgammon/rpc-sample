# -*- coding: utf-8 -*-

'''

  campaigns service

'''

# canteen
from sample.models import Campaigns
from sample.base import protect, rpc, remote


@remote.public('campaigns')
class CampaignsAPI(rpc.Service):

  ''' i manage mock campaigns '''

  @remote.public(Campaigns.Campaign, Campaigns)
  def create(self, request):

    ''' creates a campaign from a placement '''

  @remote.public(Campaigns)
  def list(self, request):

    ''' lists campaigns previously created '''
