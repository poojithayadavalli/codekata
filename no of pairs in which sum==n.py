n=int(input())
count=0
for i in range(1,n):
    for j in range(1,n):
        if i+j==n:
            count+=1
print(count)
