line= input()
n,k = line.split()
n=int(n)
k=int(k)
l=[]
for i in range(k):
    l.append(int(input()))
s=0
for el in l:
    s+=el
note_max=(s+((n-k)*3))/n
note_min=(s+((n-k)*(-3)))/n
print(str(note_min) + ' '+ str(note_max))