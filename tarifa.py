X,N,l=int(input()),int(input()),[]

for i in range(N):
    l.append(int(input()))
    
s=0
for el in l:
    s+=el

print((N+1)*X - s)