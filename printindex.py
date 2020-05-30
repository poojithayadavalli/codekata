s=input().split()
n=input().split()
def ind(n,s):
  if s in n:
  	return n.index(s)
  else:
    return -1
print(ind(n,s[1]))
