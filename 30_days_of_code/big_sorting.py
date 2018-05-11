# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 18:29:59 2018

@author: roonet4
"""

unsorted = ["3", "3", "5", "1", "10", "31411353576853", "2246537"]

def bigSorting(arr):
    
    temp_arr = arr
    temp_arr.sort()
    
    max_length = 0
    for i in range(len(temp_arr)):
        temp_length = len(temp_arr[i])
        if temp_length > max_length:
            max_length = temp_length
    
    return_array = []
    
    while max_length >= 1:
        for i in range(len(temp_arr)-1, -1, -1):
            if len(temp_arr[i]) == max_length:
                x = temp_arr.pop(i)
                return_array.insert(0, x)
        max_length -= 1
        
    return return_array


print(bigSorting(unsorted))