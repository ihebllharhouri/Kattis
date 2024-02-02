line=input()
h,P=line.split(' ')
h=int(h)
P=int(P)
i=1
n=((60-5*i)*100000)/(49*h*P)
y=int(n/143)
n=((60-5*(i+y))*100000)/(49*h*P)
print(int(n)+1)
