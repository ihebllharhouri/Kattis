from math import *
line = input()
n,w,h = line.split()
l=[]
for i in range(int(n)):
    l.append(int(input()))
for el in l:
    if el<=int(w) or el<=int(h) or el<=sqrt(int(w)*int(w) + int(h)*int(h)):
        print('DA')
    else:
        print('NE')