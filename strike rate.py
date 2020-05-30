n=int(input())
s=input().split()
l=[]
for i in range(n-1):
    x=(float(s[i])-float(s[i+1]))
    l.append(str(abs(x)))
f=(min(l))
m=l.index(f)
print(s[m],end=" ")
print(s[m+1])
#one test case
