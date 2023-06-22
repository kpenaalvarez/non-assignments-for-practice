# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:22:06 2023

@author: kpenaalvarez
"""

import numpy as np
sumOfNums=0
for i in range(1,6):
    sumOfNums += i 
# sum += is another way of saying sum = sum + 1
print(f'Average = {sumOfNums/5}\n')                          


#average with a list
nums = ( 1, 2, 3, 4, 5)
print(f'Average = {np.average(nums)}')