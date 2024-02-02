N=input()
l=[]
for i in range(int(N)):
    l.append(input())
s=0
for el in l:
    l1=el.split(' ')
    s+= float(l1[0])*float(l1[1])
print(s)
