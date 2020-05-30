n=input().split()
s=input().split()
x=int(n[1])
for j in range(x):
  temp=s[0]
  for i in range(len(s)-1):
    s[i]=s[i+1]
  s[len(s)-1]=temp
print(' '.join(s))
# one passed
