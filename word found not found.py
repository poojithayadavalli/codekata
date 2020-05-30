n=int(input())
l=[]
for i in range(n):
    l.append(input())
k=[]
for j in l:
    if j in k:
        print("Word found")
    else:
        print("Word not found , added to dictionary")
        k.append(j)
