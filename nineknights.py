liste=[]
for n in range(5):
    line=input()
    line.split()
    liste.append(line)
test= True
s=0
for i in range(5):
    for j in range(5):
        if liste[i][j]=='k':
            s+=1
for i in range(5):
    for j in range(5):
        if liste[i][j]=='k':
            if i+1<5 and j+2<5 and liste[i+1][j+2]=='k':
                test=False
            elif i+1<5 and j-2>=0 and liste[i+1][j-2]=='k':
                test=False
            elif i-1>=0 and j+2<5 and liste[i-1][j+2]=='k':
                test=False
            elif i-1>=0 and j-2>=0 and liste[i-1][j-2]=='k':
                test=False
            elif i+2<5 and j+1<5 and  liste[i+2][j+1]=='k':
                test = False
            elif i+2<5 and j-1>=0 and  liste[i+2][j-1]=='k':
                test = False
            elif i-2>=0 and j+1<5 and  liste[i-2][j+1]=='k':
                test = False
            elif i-2>=0 and j-1>=0 and liste[i-2][j-1]=='k':
                test = False
if test==True and s==9:
    print('valid')
else:
    print('invalid')