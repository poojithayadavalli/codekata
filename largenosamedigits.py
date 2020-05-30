from itertools import permutations
n = str(input())
permut_list = list(permutations(n))
l = []
for i in permut_list:
    num = i[0]
    for j in range(1, len(i)):
        num += i[j]
    l.append(int(num))
l.sort()
if l[len(l)-1] == int(n):
    print("impossible")
else:
    for i in range(len(l)-1):
        if l[i] == int(n):
            print(l[i+1])
            break
