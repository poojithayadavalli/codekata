n=int(input())
s=input().split()
h=int(s[0])
for i in range(1,n):
    h^=int(s[i])
print(h)
