l = 100000
large_prime_f = [0] * l
no_factors = [0] * l
no_factors_till = [0] * l
 
for i in range(2, l):
    if large_prime_f[i] == 0:
        for j in range(i, l, i):
            large_prime_f[j] = i
    n = large_prime_f[i]
    no_factors[i] = 1 + no_factors[i//n]
    no_factors_till[i] += no_factors[i] + no_factors_till[i-1]
 
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(no_factors_till[a] - no_factors_till[b])
