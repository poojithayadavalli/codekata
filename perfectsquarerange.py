import math
def perfect(x):
    l=int(x)
    for i in range(l):
        if(i==math.sqrt(l)):
            return True
n=input().split()
l=[]
for i in range(int(n[0]),int(n[1])+1):
    if perfect(i):
    	l.append(i)
print(len(l))
