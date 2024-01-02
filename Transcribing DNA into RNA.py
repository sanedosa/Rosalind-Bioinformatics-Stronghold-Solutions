# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 04:03:46 2023

@author: Şan
"""

dna = "GATGGAACTTGACTACGTAAATT"
rna =[]
a=""
for i in dna:
    if i=="T":
        a="U"
    else: 
        a=i
    rna.append(a)
    rnaPrint= "".join(rna)
print (rnaPrint)