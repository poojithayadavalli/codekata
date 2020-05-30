def prime(n):
    l=[]
    for k in range(n):
        if(k==2):
            l.append(str(k))
        for i in range(2,k):
            if(k%i==0):
                break
            else:
                l.append(str(k))
                break
    return l
n=int(input())
l=prime(n)
count=0
for i in range(len(l)):
    for j in range(i,len(l)):
        if(int(l[i])+int(l[j])==n):
            count+=1
print(count)

