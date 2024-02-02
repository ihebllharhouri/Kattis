N=int(input())
l=[]
for i in range(N):
    l.append(input())
l2=[]
for el in l :
    l2.append(el.split())
intervals=[]
for el in l2:
    intervals.append([int(el[0]),int(el[1])])
start,end=intervals.pop()
while intervals:
    start_temp,end_temp=intervals.pop()
    start=max(start,start_temp)
    end=min(end,end_temp)
if start>end:
    print('edward is right')
else:
    print('gunilla has a point')