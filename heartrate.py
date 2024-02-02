N=int(input())
for i in range(N):
    line=input()
    b,p=line.split()
    b=float(b)
    p=float(p)
    BPM=60*b/p
    ABPM=60/p
    print(BPM-ABPM,BPM,BPM+ABPM)