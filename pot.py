N=int(input())
l=[]
for i in range(N):
    l.append(input())
s=0
for el in l:
    s+=(int(el[0:len(el)-1])**(int(el[-1])))
print(s)
