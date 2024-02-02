line=input()
wc,hc,ws,hs=line.split()
wc,hc,ws,hs=int(wc),int(hc),int(ws),int(hs)
if (wc>=ws+2) and (hc>=hs+2):
    print(1)
else:
    print(0)