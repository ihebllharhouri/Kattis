n=int(input())
test=False
m=2
while test==False and m<n:
    cpt=0
    for k in range(2,(n*m)//4):
        if (n*m)%(k*k)==0:
            cpt+=1
    if cpt!=0:
        m+=1
    else:
        test=True
print(m)
    