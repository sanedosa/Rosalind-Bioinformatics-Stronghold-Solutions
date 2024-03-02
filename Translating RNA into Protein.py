


prot=[]
codon=[]
f =open("rosalind_prot.txt", "r")
string=f.read()
# string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
table = {"UUU":"F",     "CUU": "L",      "AUU": "I",      "GUU":" V",
"UUC" :"F",      "CUC": "L",      "AUC": "I",      "GUC" :"V",
"UUA" :"L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
"UUG" :"L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
"UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU" :"A",
"UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA" :"A",
"UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"UAU":"Y",     "CAU" :"H",      "AAU":"N",      "GAU": "D",
"UAC":"Y",      "CAC":"H",      "AAC":"N",      "GAC":"D",
"UAA":"Stop",  "CAA": "Q",      "AAA": "K",     "GAA":"E",
"UAG":"Stop",  "CAG" :"Q",     "AAG": "K",     "GAG":"E",
"UGU": "C",    "CGU": "R",     "AGU": "S",     "GGU":"G",
"UGC":"C",    "CGC": "R",     "AGC": "S",     "GGC":"G",
"UGA": "Stop",  "CGA": "R",     "AGA": "R",     "GGA":"G",
"UGG":"W",    "CGG": "R",     "AGG" :"R",     "GGG":"G", }

for i in range(0, len(string), 3) :
    codon.append(string[i])
    codon.append(string[i+1])
    codon.append(string[i+2])
    codonprint="".join(codon)
    if table[codonprint] == "Stop":
        break
    prot.append(table[codonprint])
    codon=[]
        
protPrint="".join(prot)
    

print(protPrint)
