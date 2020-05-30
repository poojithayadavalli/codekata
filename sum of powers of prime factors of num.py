def factors(n):
    i = 2
    factors = []
    while i <= n:
        if (n % i) == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors
x=int(input())
y=factors(x)
count=len(set(y))
l=[]
for j in y:
    if j in l:
        count+=1
    else:
        l.append(j)
print(count)
        
    
