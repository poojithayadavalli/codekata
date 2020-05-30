x=input()
y=[int(x)for x in input().split()]
y.sort()
y=[str(x)for x in y]
print("".join(y[::-1]))
