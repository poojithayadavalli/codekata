def reverse(x):
    return x[::-1]
n=input().split()
for i in range(len(n)):
    if i%2==0:
        n.append(reverse(n[i]))
    else:
        n.append(n[i])
print(' '.join(n))
