def factors(n):
    factors = []
    for i in range(1,n+1):
        if (n % i) == 0:
            factors.append(i)
    return factors
x=int(input())
y=list(map(str,factors(x)))
print(' '.join(y))
        
    
