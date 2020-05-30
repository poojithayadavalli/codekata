n=int(input())
arr=list(map(int,input().split()))
m = 1
temp = 1
for i in range(1, n):
    if (arr[i] > arr[i-1]):
        temp+=1
    else:
        if(m < temp):
            m = temp
        temp= 1
if (m<temp):
    m = temp
print(m if m>1 else"-1")

