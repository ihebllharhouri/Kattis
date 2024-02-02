liste=[]
for i in range(3):
    line=input()
    a,b=line.split()
    a=int(a)
    b=int(b)
    liste.append([a,b])

def flip(lstt):
    lstt1=[0,0]
    aux=lstt[0]
    lstt1[0]=lstt[1]
    lstt1[1]=aux
    return lstt1

def carre(listee):
    if listee[0][0]==listee[1][0] and listee[1][0]==listee[2][0]:
        if listee[0][1]+listee[1][1]+listee[2][1]==listee[0][0]:
            return True
        else:
            return False
    if listee[0][0]==listee[1][0] and listee[0][1]+listee[1][1]==listee[2][0] and listee[0][0]+listee[2][1]==listee[2][0]:
        return True
    if listee[0][0]==listee[2][0] and listee[0][1]+listee[2][1]==listee[1][0] and listee[0][0]+listee[1][1]==listee[1][0]:
        return True
    if listee[2][0]==listee[1][0] and listee[2][1]+listee[1][1]==listee[0][0] and listee[1][0]+listee[0][1]==listee[0][0]:
        return True
    return False



liste2= [liste[0],liste[1],flip(liste[2])]
liste3 = [liste[0], flip(liste[1]), liste[2]]
liste4 = [liste[0], flip(liste[1]), flip(liste[2])]
liste5 = [flip(liste[0]), liste[1], liste[2]]
liste6 = [flip(liste[0]), liste[1], flip(liste[2])]
liste7 = [flip(liste[0]), flip(liste[1]), liste[2]]
liste8 = [flip(liste[0]), flip(liste[1]), flip(liste[2])]
test1 = carre(liste)
test2 = carre(liste2)
test3 = carre(liste3)
test4 = carre(liste4)
test5 = carre(liste5)
test6 = carre(liste6)
test7 = carre(liste7)
test8 = carre(liste8)

test=test1 or test2 or test3 or test4 or test5 or test6 or test7 or test8
if test==True :
    print('YES')
else:
    print('NO')









