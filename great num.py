n=int(input())
n=str(n)
s=0
p=1
for i in range(len(n)):
  s=s+int(n[i])
  p=p*int(n[i])
r=s+p
if(r==int(n)):
  print("Great")
else:
  print("no")
