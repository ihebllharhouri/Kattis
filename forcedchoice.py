line=input()
N,P,S=line.split()
N,P,S=int(N),int(P),int(S)
liste=[]
for i in range(S):
    line=input()
    liste1=line.split()
    liste1.remove(liste1[0])
    liste.append(liste1)

for el in liste:
    if str(P) in el:
        print('KEEP')
    else:
        print('REMOVE')
