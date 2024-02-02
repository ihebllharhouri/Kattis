ch=input()
i=0
test=True
while test==True and i<len(ch):
    if ch[i]=='a':
        test=False
    else:
        i+=1


print(ch[i:])
