k=int(input())
n=3
m=4
for i in range(1,k+1):
    m-=1
    if m==0:
        m=n*2
        n=m
print(m)
