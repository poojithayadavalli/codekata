from itertools import permutations
s=list(input())
perm=permutations(s)
h=list(perm)
for i in h:
  print(''.join(i))
