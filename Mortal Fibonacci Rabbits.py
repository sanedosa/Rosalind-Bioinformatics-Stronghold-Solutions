

# Derived from: https://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html

n=89
m=17

alive=[1,1]

for i in range(2,n):

    if i < m:
        alive.append(alive[-2]+alive[-1])
        
    elif i == m:
        alive.append(alive[-2]+alive[-1] -1 )
    else:
        alive.append(alive[-2]+alive[-1] - alive[-(m + 1)] )
    
print(alive[-1])
