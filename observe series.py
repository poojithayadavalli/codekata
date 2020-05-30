x=int(input())
l=[]
if x>1:
    l.append(str("0"))
    for i in range(1,x+1):
        l.append(str((i**3)+int(l[i-1])))
    print(' '.join(l[1:]))
else:
  print("-1")
#one
