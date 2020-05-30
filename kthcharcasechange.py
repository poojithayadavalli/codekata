n=input().split()
k=int(n[1])
n1=list(n[0])
for i in range(k-1,len(n1),k):
    n1[i]=n1[i].upper()
print(''.join(n1))
#incomplete
