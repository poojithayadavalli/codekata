x=int(input())
l=[]
while x>0:
  if x==1:
    l.append(x)
    x=0
  else:
    l.append(x%2)
    x=x//2
m=[str(i) for i in l[::-1]]
print(''.join(m))
