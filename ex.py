n=int(input())
s=input()
x=sorted(s)
l=x[:len(x)-n]
print(''.join(l))
