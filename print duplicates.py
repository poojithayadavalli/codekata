x=input()
l=[]
m=[]
for i in x:
  if i in l:
    m.append(i)
  else:
    l.append(i)
m=set(m)
print(' '.join(m))
