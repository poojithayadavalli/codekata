x=input()
y=input().split()
z=[]
for i in y:
    if i in z:
        pass
    else:
        z.append(i)
print(' '.join(z))
