n,l,r=map(int,input().split())
n=bin(n)[2:]
#print(n)
x=["1" for i in range(l,r+1)]
n=[str(i)for i in n]
n[l:r+1]=x
y=''.join(n)
print(int(y,2))
