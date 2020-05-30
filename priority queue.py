n=int(input())
s=input().split()
l=[]
for i in range(n):
  l.append(s[i])
  print(min(l),end=" ")
