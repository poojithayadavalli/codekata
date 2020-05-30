n=int(input())
s=list(map(int,input().split()))
e=0
o=0
for i in s:
    if i%2==0:
        e+=1
    else:
        o+=1
if(e>o):
    print((e-o)//2)
else:
    print((e-o))
    #one
        
