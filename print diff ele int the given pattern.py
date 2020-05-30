x=input()
l = list(map(int,input().split()))
c= [] 
for i in l:
  if i%2==0:
    c.append(1)
  else:
    c.append(0)
if c.count(1)==1:
  print(l[c.index(1)])
elif c.count(0)==1:
  print(l[c.index(0)])
else:
  print("-1")
