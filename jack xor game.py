n,q=map(int,input().split())
l=list(map(int,input().split())) 
for _ in range(q):
    t=int(input())
    t=list(bin(t))
    t.pop(0)
    t.pop(0)
    res=[]
    for i in range(len(l)):
        k=list(bin(l[i]))
        k.pop(0)
        k.pop(0)
        if(len(k)>len(t)):
            t.reverse()
            for j in range(len(k)-len(t)):
                t.append("0") 
            t.reverse()
        elif(len(t)>len(k)):
            k.reverse()
            for j in range(len(t)-len(k)):
                k.append("0") 
            k.reverse() 
        z=""
        for j in range(len(k)):
            if(k[j]==t[j]):
                z=z+"0"
            else:
                z=z+"1" 
        res.append(int(z,2)) 
    print(max(res))
