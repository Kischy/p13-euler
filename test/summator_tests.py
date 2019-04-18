# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:46:20 2019

@author: Kischy
"""

import sys
sys.path.insert(0, "../src/")

import unittest
import summator


class TestSummator(unittest.TestCase):
    
    def setUp(self):
        self.summator = summator();

