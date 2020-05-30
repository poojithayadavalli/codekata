n=input().split()
flag=False
for i in range(len(n)):
    for j in range(1,len(n[i])):
        if n[i][0].isupper() and n[i][j].islower():
            flag=True
print("yes" if flag else "no")
