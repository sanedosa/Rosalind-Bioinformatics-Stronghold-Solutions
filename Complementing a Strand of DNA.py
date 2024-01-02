# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:37:12 2023

@author: Şan
"""

dna="AAAACCCGGT"
comp=[]
a=""
dnalen=len(dna)
print(dnalen)

for dnalen in dna:
    if dnalen=="T":
        a="A"
    elif dnalen=="A":
        a="T"
    elif dnalen=="C":
        a="G"
    elif dnalen=="G":
        a="C"
    comp.append(a)
compprint= "".join(comp)
rev=compprint[::-1]
print(rev)
    
        