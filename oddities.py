n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
for el in l:
    if el%2==0:
        print( str(el)+' is even')
    else:
        print( str(el)+' is odd')