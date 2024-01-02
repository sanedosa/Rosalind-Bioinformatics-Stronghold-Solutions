# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:59:01 2023

@author: Şan
"""

n=32
k=5
f1=1
f2=1



for i in range(n-2):
  f3=f1+f2*k
  f2=f1
  f1=f3
  
   
print(f3)

