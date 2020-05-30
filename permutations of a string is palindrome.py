from itertools import permutations 
l=[]
def allPermutations(str1):
    permList = permutations(str1)
    for perm in list(permList):
        l.append(''.join(perm))
    return l
x=input()
y=allPermutations(x)
y.sort()
flag=flag=False
for i in y:
    t=i[::-1]
    if t==i:
        print(t)
        flag=True
        break
if not flag:
    print("no")
