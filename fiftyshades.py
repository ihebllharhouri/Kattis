n=int(input())
s=0
for i in range(n):
    line=input()
    if ('pink'.upper() in line.upper()) or ('rose'.upper() in line.upper()):
        s+=1

if s==0:
    print('I must watch Star Wars with my daughter')
else:
    print(s)