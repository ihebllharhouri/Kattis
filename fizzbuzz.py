line=input()
x,y,n=line.split()
x,y,n=int(x),int(y),int(n)
for i in range(1,n+1):
    if i%x==0 and i%y !=0:
        print('Fizz')
    elif i%y==0 and i%x !=0:
        print('Buzz')
    elif i%x==0 and i%y==0:
        print('FizzBuzz')
    else:
        print(str(i))
