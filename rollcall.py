import sys
l=[]
for line in sys.stdin:
    l.append(line)
l1,l2=[],[]
for el in l:
    liste=el.split()
    l1.append(liste[0])
    l2.append(liste[1][0:])

liste=[]
for i in range(len(l1)):
    liste.append([l2[i],l1[i]])

liste_sorted = sorted(liste)

for i in range(len(liste_sorted)):
    x=liste_sorted[i][1]
    s=0
    for el in liste_sorted:
        if el[1]==x:
            s+=1
    if s>=2:
        print(x+' '+ liste_sorted[i][0])
    else:
        print(x)

