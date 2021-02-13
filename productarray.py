#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Product of an Array"""

def productArray(arr, n):  
  
    if(n == 1): 
        print(0) 
        return
   
    prod = [0]*n  
  
    for i in range(1, n):  
        prod_temp[i] = arr[i - 1] * prod_temp[i - 1]  
    
    for i in range(n):  
        prod[i] = prod_temp[i]
 
    for i in range(n):  
        print(prod[i], end =' ')  
 