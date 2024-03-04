

s="TTAGTCAATAATACGTGACGTTGTCGGATCGAGGAAGATGCATCCGAGAAGGGATGTGATGAAGGGCGTTTAAGGTTTGAACCGCACATAGCAGTTGTTCGACTGTACGTCAACTGGGGAACTGGCCACACCTTGATCGTTTTCGGGACAGGACAGCATCCTTAAACACCGGTGAGGAGAAACCAATGCTGGTAACATATCGTATTTAGTCCGAACTTTACGCCAGTATTGTTTTGTCACTTAAACGTATCGTGAGCTAGCAACACAGGCTCGTGGGACTTGATGCGGCCCCCGACAACAAAGCAAGCTATGAACTAGAATGCTTCGGGGCATCCTAAGATCGTATTTATTTAAATATTGTGGCAGGCTACTTTCAGTAAGCAACAATGTATCGGAGAATATGAGATCACAGGGGTTAACAACTTCGTAGCTACGAAGTTGTTAACCCCTGTGATCTCATGAGTTAGGGTAGCATCAGTTAGTGGAGTTCGGCTCGAGGGCTACGATCAGCTGGTCAGAGAGTAAGTTGTAGTCCTCCCTGGAACCGTGCTCTGTTACCCACCCATCTCAAAAGGTCAAGCTCCGCATTGATATCATAAAGACGATAGACTCAGCTGAGCAATCGCACGATCACTGAGCTCCCTGTGGCGGATACACCCGACTGATTACTACGGTACAGTACCGGACGTTCTATTCCTATACCTGCCTGTTTAGGTTTGATTGACCGATTGCACTTACAAGACCCAATGCTCCGCTGCAGTGCGTATTAACAATGATTTGGCTGGCTGCGTGCTGTGACAAGCAGAAGAGCAAACCAACGACTAAGCTTTGGAACTATTATTGTCAATCAAAGAGGAAGC"
# rev="CTGAGATGCTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTCTAATCCAAGTCGCGGGGTCATCCCCATGTAACCTGAGTTAGCTACATGGCT"
orf=[]

prot=[]
codon=[]
# f =open("rosalind_prot.txt", "r")
# string=f.read()

dna=s
comp=[]
a=""
dnalen=len(dna)


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


table = {"TTT":"F",     "CTT": "L",      "ATT": "I",      "GTT":"V",
"TTC" :"F",      "CTC": "L",      "ATC": "I",      "GTC" :"V",
"TTA" :"L",      "CTA": "L",      "ATA": "I",      "GTA": "V",
"TTG" :"L",      "CTG": "L",      "ATG": "M",      "GTG": "V",
"TCT": "S",      "CCT": "P",      "ACT": "T",      "GCT" :"A",
"TCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"TCA": "S",      "CCA": "P",      "ACA": "T",      "GCA" :"A",
"TCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"TAT":"Y",     "CAT" :"H",      "AAT":"N",      "GAT": "D",
"TAC":"Y",      "CAC":"H",      "AAC":"N",      "GAC":"D",
"TAA":"Stop",  "CAA": "Q",      "AAA": "K",     "GAA":"E",
"TAG":"Stop",  "CAG" :"Q",     "AAG": "K",     "GAG":"E",
"TGT": "C",    "CGT": "R",     "AGT": "S",     "GGT":"G",
"TGC":"C",    "CGC": "R",     "AGC": "S",     "GGC":"G",
"TGA": "Stop",  "CGA": "R",     "AGA": "R",     "GGA":"G",
"TGG":"W",    "CGG": "R",     "AGG" :"R",     "GGG":"G", }

for i in range(0, len(s)):
    if s[i:i+3]== "ATG":
        for m in range(0, len(s[i:])-3,3):
            codon.append(s[i+m])
            codon.append(s[i+1+m])
            codon.append(s[i+2+m])
            codonprint="".join(codon)
            
            
            codon=[]
            if table[codonprint] == "Stop":
                
                orf.append("".join(prot))
                break
            else:
                prot.append(table[codonprint])
        prot=[]

for i in range(0, len(rev)):
    if rev[i:i+3]== "ATG":
        for m in range(0, len(rev[i:])-3,3):
            codon.append(rev[i+m])
            codon.append(rev[i+1+m])
            codon.append(rev[i+2+m])
            codonprint="".join(codon)
            
            codon=[]
            if table[codonprint] == "Stop":
                
                orf.append("".join(prot))
                break
            else:
                prot.append(table[codonprint])
            
        
        prot=[]
for i in set(orf):
    print(i)