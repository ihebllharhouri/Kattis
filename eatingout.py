line=input()
m,a,b,c=line.split()
m=int(m)
a=int(a)
b=int(b)
c=int(c)
if a+b+c>2*m:
    print('impossible')
else:
    print('possible')
    