s1,s2 = input().split()
dic1 = {}
res = 'yes'
for i in range(0,len(s1)) :
    c1,c2 = s1[i], s2[i]
    if c1 not in dic1 and c2 not in dic1:
        dic1[c1] = c2
        dic1[c2] = c1
    elif c1 in dic1 and dic1[c1] == c2 :
        pass
    else :
        res = 'no'
        break
print(res,end='')
