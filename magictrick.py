s=input()
test=True
i=0
while (test==True) and (i<len(s)):
    if s.count(s[i])>1:
        test=False
    else:
        i+=1
if test==False:
    print(0)
else:
    print(1)
