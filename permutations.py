from itertools import permutations
n=int(input())
s=input().split()
perm=permutations(s)
h=list(perm)
print(''.join(max(h)))
