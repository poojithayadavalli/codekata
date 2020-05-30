n=int(input())
s=[]
for i in range(n):
    x=input()
    s.append(input().split())
for i in range(n-1):
    s[i].sort()
    print(' '.join(s[i]),end=" ")
s[n-1].sort()
print(' '.join(s[n-1]))
