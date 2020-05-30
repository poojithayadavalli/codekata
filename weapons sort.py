L = []
try:
    while True:
        a,b =[x for x in input().split()]
        L.append((a,int(b)))
except:
    pass
finally:
    L.sort(key=lambda x : x[1])
    for i in range(len(L)):
        print(i+1,L[i][0])
