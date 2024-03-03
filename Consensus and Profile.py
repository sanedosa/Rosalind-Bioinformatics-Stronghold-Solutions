

# f =open("test.txt", "r")
# dna=[]
# for i in f.read().splitlines():
#     if i[0]!=">":
        
#         dna.append(i)

f =open("rosalind_cons.txt", "r")
list = f.read().splitlines()


dna=[]
for line in "".join(list).split(">")[1:]:
    dna.append(line[13:])


A=[]
C=[]
G=[]
T=[]
consensus=[]
dic={"A":0, "C":0, "G":0, "T":0}
for n in range(0, len(dna[0])):
    for i in range(0, len(dna)):
        dic[dna[i][n]]+=1
    A.append(dic.get("A"))
    C.append(dic.get("C"))
    G.append(dic.get("G"))
    T.append(dic.get("T"))
    consensus.append(max(dic, key=dic.get))
    dic={"A":0, "C":0, "G":0, "T":0}

print("".join(consensus))
print("A:", " ".join(map(str, A)))
print("C:", " ".join(map(str, C)))
print("G:", " ".join(map(str, G)))
print("T:", " ".join(map(str, T)))


