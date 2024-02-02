import sys

data = sys.stdin.readlines()
vierge=[]
vierge2=[]
for el in data:
    if el[-1::]=='\n':
        ch=el[0:len(el)-1]
        liste=ch.split(" ")
        for el1 in liste:
            if el1.lower() in vierge:
                vierge.append('.')
                vierge2.append('.')
            else:
                vierge.append(el1.lower())
                vierge2.append(el1)
        vierge2.append("\n")
    else:
        ch = el
        liste = ch.split(" ")
        for el1 in liste:
            if el1.lower() in vierge:
                vierge.append('.')
                vierge2.append('.')
            else:
                vierge.append(el1.lower())
                vierge2.append(el1)
        vierge2.append("\n")


final=""
for el in vierge2:
    if el=='\n':
        final+=el
    else:
        final+=el+' '
final2=final[:-1]
print(final2)