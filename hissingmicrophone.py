s=input()
test=False
for i in range(len(s)-1):
    if s[i]=='s':
        if s[i+1]=='s':
            test=True
if test==True:
    print('hiss')
else:
    print('no hiss')


