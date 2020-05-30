n=input().split()
x=int(n[1])
count=0
f=1
for i in range(x):
    if int(n[0][i]) not in range(0,x+1):
        break
    else:
        f=0
print("yes" if f==0 else "no")
        
