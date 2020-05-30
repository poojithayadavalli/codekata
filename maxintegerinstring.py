n=list(map(list,input().split()))
for i in n:
  if '.'in i:
    i.remove('.')
l=[]
y=[''.join(x) for x in n]
for i in y:
    if i.isdigit():
    	l.append(i)
l=[int(x) for x in l]
print(max(l))
