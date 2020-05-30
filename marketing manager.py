t=int(input())
for z in range(0,t):
  n=int(input())
  l1=list(map(int,input().split())) 
  l2=list(map(int,input().split())) 
  ind=0
  for I in range(0,len(l1)):
    if(l1[I] not in l2):
      ind=I
      break
  print(ind) 
