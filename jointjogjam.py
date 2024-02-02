from math import sqrt
line=input()
l=line.split()
for i in range(len(l)):
    l[i]=int(l[i])
d1=sqrt((l[2]-l[0])**2+(l[3]-l[1])**2)
d2=sqrt((l[6]-l[4])**2+(l[7]-l[5])**2)
if d1<d2:
    print(d2)
else:
    print(d1)
