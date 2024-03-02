


# k=19 #dominant
# l=21 #heterozygous
# m=18 #homozygous recessive

# prob= (m/(k+l+m))*(l/(k+l+(m-1)))*(1/2) + (m/(k+l+m))*(k/(k+l+(m-1))) + (l/(k+l+m))* (m/(k+(l-1)+m)) * (1/2) + (l/(k+l+m))* ((l-1)/(k+(l-1)+m)) * (3/4) + (l/(k+l+m))*(k/(k+(l-1)+m)) + k/(k+l+m)
def Mendel (k,l,m):
    N=k+l+m

    prob= ((m/N)*(l/(N-1))*(1/2) + (m/N)*(k/(N-1)) + 
        (l/N)* (m/(N-1)) * (1/2) + (l/(N))* ((l-1)/(N-1)) * (3/4) + (l/N)*(k/(N-1)) + 
        k/N)
    return(prob)

print(Mendel(19,21,18))
