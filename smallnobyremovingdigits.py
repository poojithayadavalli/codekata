x=input().split()
n=int(x[1])
s=x[0]
l=[]
try:
    for i in range(n+1):
    	x=s
    	l.append(int(x[i:len(s)-n+i]))
    print(min(l))
except:
    print("0")
#one test
