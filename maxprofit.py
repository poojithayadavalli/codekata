n=int(input())
s=input().split()
l=[]
for i in range(n-1):
    for j in range(i+1,n):
    	l.append(int(s[j])-int(s[i]))
print(max(l))
