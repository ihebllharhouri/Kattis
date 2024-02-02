n=int(input())
l=[]
for i in range(n):
    l.append(input())
for el in l:
    l1=el.split(' ')
    if int(l1[0])< (int(l1[1])- int(l1[2])):
        print('advertise')
    elif  int(l1[0])== (int(l1[1])- int(l1[2])):
        print('does not matter')
    else:
        print('do not advertise')