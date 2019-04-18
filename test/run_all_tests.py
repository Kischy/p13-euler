# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:40:57 2019

@author: Kischy
"""

import unittest

# import test modules
import summator_tests

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()


# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(summator_tests))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
