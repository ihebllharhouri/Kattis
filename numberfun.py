n=input()
n=int(n)

for i in range(n):
    line=input()
    a,b,c=line.split()
    a,b,c=int(a),int(b),int(c)
    if a+b==c or abs(a-b)==c or a*b==c or a/b==c or b/a==c:
        print('Possible')
    else:
        print('Impossible')