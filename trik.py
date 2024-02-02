line=input()
s=1
for chr in line:
    if s==1 and chr=='A':
        s=2
    elif s==1 and chr=='C':
        s=3
    elif s==1 and chr=="B":
        s=1
    elif s==2 and chr=='A':
        s=1
    elif s==2 and chr=='B':
        s=3
    elif s==2 and chr=="C":
        s=2
    elif s==3 and chr=="A":
        s=3
    elif s == 3 and chr == "B":
        s=2
    elif s == 3 and chr == "C":
        s=1
print(s)


