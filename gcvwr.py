l=(input().split())
l1=input().split(' ')
G_T=(int(l[0])-int(l[1]))
s=0
for el in l1:
    x=int(el)
    s+=x
print(int((G_T*0.9 - s)))