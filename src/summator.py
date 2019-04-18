# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:40:57 2019

@author: Kischy
"""


class Summator():
    
    def sum_num(self,number):     
        
        if(len(number) == 0):
            return 0
        
        the_sum = 0       
    
        number = number.split("\n")
        
        for num in number:
            if(num != ""):
                the_sum += int(num)
        
        return the_sum


    
    

