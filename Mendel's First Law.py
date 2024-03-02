


k=19 #dominant
l=21 #heterozygous
m=18 #homozygous recessive
total=k+l+m
# prob= (m/(k+l+m))*(l/(k+l+(m-1)))*(1/2) + (m/(k+l+m))*(k/(k+l+(m-1))) + (l/(k+l+m))* (m/(k+(l-1)+m)) * (1/2) + (l/(k+l+m))* ((l-1)/(k+(l-1)+m)) * (3/4) + (l/(k+l+m))*(k/(k+(l-1)+m)) + k/(k+l+m)
prob= ((m/total)*(l/(total-1))*(1/2) + (m/total)*(k/(total-1)) + 
       (l/total)* (m/(total-1)) * (1/2) + (l/(total))* ((l-1)/(total-1)) * (3/4) + (l/total)*(k/(total-1)) + 
       k/total)
print(prob)