s = input()
n = len(s)
dic1={}
oddf = 0
for c in s :
    dic1[c] = dic1.get(c,0)+1
for k,v in dic1.items() :
    if v%2==1 :
        oddf += 1
res = 'NO'
if n%2==1 :
    if oddf==1 or oddf==3 :
        res = 'YES'
else :
    if oddf==2 :
        res = 'YES'
print(res,end='')
