from itertools import permutations
s=list(input())
l=[]
perm=permutations(s)
h=list(perm)
for i in h:
  l.append(''.join(i))
x=list(map(int,l))
print(sum(x))
