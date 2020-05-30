n=int(input())
l=[]
flag=False
for i in range(n):
    l.append(input().split())
for i in range(n-1):
    for j in range(i+1,n):
        if l[i][0]==l[j][1] and l[i][1]==l[j][0]:
            flag=True
            break
print("YES" if flag else "NO")
