import sys
s = input()
L1 = []
L2 = []
n = len(s)
i=0
while i < n :
    L1.append(s[i])
    i += 1
    s3=''
    while s[i].isdigit() :
        s3 += s[i]
        i += 1
        if i == n:
            break
    L2.append(int(s3))
    if i==n :
        break
L3 = []
for i in range(len(L1)) :
    if L2[i]%2==1 :
        L3.append(L1[i]+str(L2[i]))
    else :
        L3.append(L1[i] * L2[i])

res = ''.join(L3)
print(res,end='')
