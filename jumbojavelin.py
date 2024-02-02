N=int(input())
l=[]
for i in range(N):
    l.append(int(input()))
s=0
for el in l:
    s+=el
print(s-(N-1))