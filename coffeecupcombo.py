n=int(input())
s=input()
tot_wake_time=0
coffe_left=0
for i in range(n):
    if s[i]=="1":
        coffe_left=2
        tot_wake_time+=1
    elif coffe_left>0:
        coffe_left-=1
        tot_wake_time+=1
print(tot_wake_time)

