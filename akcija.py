n=int(input())
liste=[]
for i in range(n):
    x=int(input())
    liste.append(x)
liste2=sorted(liste,reverse=True)
somme=0
for el in liste:
    somme+=el
j=2
while j<n:
    somme=somme-liste2[j]
    j+=3
print(somme)
