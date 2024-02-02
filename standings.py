t=int(input())
for i in range(t):
    space=input()
    n=int(input())
    ints = []
    for j in range(n):
        line=input()
        ch,x=line.split()
        ints.append(int(x))
    ints.sort()
    err=0
    for l in range(n):
        err+= max(l+1-ints[l],ints[l]-l-1)
    print(err)



