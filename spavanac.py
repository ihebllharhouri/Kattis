ch=input()
liste=ch.split(' ')
liste2=[]
for el in liste:
    liste2.append(int(el))
if liste2[1]>=45:
    print(str(liste2[0])+' '+str(liste2[1]-45))
elif liste2[1]<45 and liste2[0]==0:
    print('23 '+str(60-(45-liste2[1])))
else:
    print(str(liste2[0]-1)+' '+str(60-(45-liste2[1])))

