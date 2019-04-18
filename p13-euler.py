# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:40:57 2019

@author: Kischy
"""

import sys
sys.path.insert(0, "src/")


from summator import Summator as SM
import the_number


sm = SM()


print("Calculation started")

p13_answ = sm.sum_num(the_number.the_number)


p13_answ = str(p13_answ)[:10]



print("The answer to the 13th problem of ProjectEuler.Net is:",p13_answ)
