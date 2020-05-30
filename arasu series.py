def isprime(x):
    if x>1:
        if x==2:
            return True
        else:
            for j in range(2,x):
                if(x%j)==0:
                    flag=False
                    break
                else:
                    flag=True
            return flag
    else:
        return False
n=int(input())
count=0
num=2
l=[]
sum1=0
while(count<n):
    if isprime(num):
        l.append(num)
        num+=1
        count+=1
    else:
        num+=1
#print(l)
for i in range(n):
    sum1+=l[i]
    print(sum1,end=" ")
    
    
    
