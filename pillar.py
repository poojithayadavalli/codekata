n=int(input())
s=[int(i)for i in input().split()]
count=1
x=s[0]
for i in range(1,len(s)):
    if x<s[i]:
        count=count+1
        x=s[i]
print(count)
