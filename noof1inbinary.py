n=int(input())
s=bin(n)
count=0
for i in s:
    if i=='1':
        count+=1
print(count)
