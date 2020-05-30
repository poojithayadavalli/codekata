n=int(input())
x=input().split()
l=[]
for i in range(n-1):
    for j in range(i+1,n):
        m=abs(int(x[j])-int(x[i]))
        l.append(str(m))
print(max(l))
