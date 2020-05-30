n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(len(l)):
    r.append(str(l.index(i+1)+1)) 
print(" ".join(r))
