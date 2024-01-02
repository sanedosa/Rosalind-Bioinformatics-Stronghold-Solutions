# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 04:03:11 2023

@author: Şan
"""

string="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

freq={"A":0, "T":0, "G":0, "C":0}
for i in string:
    freq[i] = freq[i] +1
    
print(freq["A"], freq["G"], freq["C"], freq["T"])

    