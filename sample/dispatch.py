# -*- coding: utf-8 -*-

'''

  canteen RPC sample: WSGI gateway

'''

# WSGI spawn
import canteen, sample; application = canteen.spawn(sample, dev=__debug__, config=sample.config.config)
