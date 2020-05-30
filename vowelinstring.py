n=int(input())
l=[]
for i in range(n):
    l.append(input())
flag=0
for i in range(n):
    for j in range(len(l[i])):
        if l[i][j] in ['a','e','i','o','u']:
            flag+=1
            break
print("yes" if flag==n else "no")
