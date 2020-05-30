def ex(l):
    count=0
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            for k in range(j+1,len(l)):
                if int(l[i])+int(l[j])==int(l[k]):
            	    count+=1
    return count
x=input()
y=input().split()
print(ex(y))
