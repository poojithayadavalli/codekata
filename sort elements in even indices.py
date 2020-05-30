def evenOddSort(inp):
    l=[]
    evens = [ inp[i] for i in range(0,len(inp)) if i%2==0 ]  
    odds = [ inp[i] for i in range(0,len(inp)) if i%2!=0 ]
    evens.sort()
    if len(evens)>len(odds):
        for i in range(len(evens)-1):
            l.append(evens[i])
            l.append(odds[i])
        l.append(evens[len(evens)-1])
    else:
        for i in range(len(evens)):
            l.append(evens[i])
            l.append(odds[i])
    m=list(map(str,l))
    return ' '.join(m)
x=input()
y=list(map(int,input().split()))
print(evenOddSort(y))
#one
