#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:38 2018

@author: Anastasia
"""
#%%
def linear(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i 
        
    return None 


#%%

def hello():
    name = input ( "whats your name?")
    print ("hello" + name)
    