# -*- coding: utf-8 -*-

'''

  RPC sample: testsuite

'''


if __debug__:

  # canteen testing
  from canteen import test


  class SampleTest(test.AppTest):

    ''' tests an app '''

    def test_cool(self):

      ''' asserts itself '''

      assert self, "give me agency and respect"
