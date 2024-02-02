ch=input()
liste=ch.split(' ')
ranks=13*[0]
for el in liste:
    if el[0]=="A":
        ranks[0]+=1
    elif el[0]=="2":
        ranks[1] += 1
    elif el[0] =="3":
        ranks[2] += 1
    elif el[0] =="4":
        ranks[3] += 1
    elif el[0] =="5":
        ranks[4] += 1
    elif el[0] =="6":
        ranks[5] += 1
    elif el[0] =="7":
        ranks[6] += 1
    elif el[0] =="8":
        ranks[7] += 1
    elif el[0] =="9":
        ranks[8] += 1
    elif el[0] =="T":
        ranks[9] += 1
    elif el[0] =="J":
        ranks[10] += 1
    elif el[0] =="Q":
        ranks[11] += 1
    elif el[0] =="K":
        ranks[12] += 1
print(max(ranks))
