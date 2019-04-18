# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:46:20 2019

@author: Kischy
"""

import sys
sys.path.insert(0, "../src/")

import unittest
from summator import Summator


class TestSummator(unittest.TestCase):
    
    def setUp(self):
        self.summator = Summator();
    
    
    def test_gives_back_zero_on_empty_string(self):
        self.assertEqual(self.summator.sum_num(""),0)
        
    def test_raises_ValueError_on_character_string(self):
        with self.assertRaises(ValueError):
            self.summator.sum_num("008a87uds")

    def test_gives_back_correct_sum_123_and_3545(self):
        self.assertEqual(self.summator.sum_num("123\n3545"),3668)

    def test_gives_back_correct_sum_94801234_and_8_and_938(self):
        self.assertEqual(self.summator.sum_num("94801234\n8\n938"),94802180)

