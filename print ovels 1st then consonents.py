s = input()
L1 = []
L2 = []
for c in s :
    if c in 'aeiouAEIOU' :
        L1.append(c)
    else :
        L2.append(c)
res = ''.join(L1) + ''.join(L2)
print(res,end='')
