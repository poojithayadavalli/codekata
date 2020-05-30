n = int(input())
sieve = [True] * (n+1)
sieve[0] = False
sieve[1] = False
 
i = 2
while i*i < n:
    if sieve[i]:
        for j in range(i+i, n+1, i):
            sieve[j] = False
    i += 1
 
for num in range(2, n//2+1):
    if sieve[num] and sieve[n - num]:
        print(num, n-num)
        break
