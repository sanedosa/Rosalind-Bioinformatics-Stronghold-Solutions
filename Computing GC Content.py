# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:58:03 2023

@author: Şan
"""


def GC(data):
    # GCscore=0
    # ATscore=1
    # scores=[]
    number=0
    perc1=0
    # ID= ""
    for x in data:
        GCscore=0
        ATscore=0
        
        
        # print(number)
        for i in data[number]:
            if i=="C" or i=="G":
                GCscore=GCscore+1
            if i=="A" or i=="T":
                ATscore=ATscore+1
        perc2=GCscore/(GCscore+ATscore)*100
        if perc2 > perc1:
            perc1=perc2
            ID=data[number][:13]
        
        # scores.append(data[number][:13])
        # scores.append(perc2)
        number=number+1
        
    #print(scores)
    print(ID)
    print(perc1)
    
f =open("rosalind_gc (1).txt", "r")
dna=f.read().strip("/n")
dnalist=dna.split(">")
dnalist=dnalist[1:]
# print(dnalist)


# for i in dnalist[1]:
#     if i=="C":
#         score=score+1



            
GC(dnalist)

