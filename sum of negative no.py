n=int(input())
x=input().split()
s=0
for i in x:
    if int(i)<0:
        s+=int(i)
print(s)
