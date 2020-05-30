n = int(input())
arr = ''.join(input().split())
 
mid = n//2 - 1
res = ''
 
for i in range(mid, -1, -1):
    if arr[i] == arr[n-1-i]:
        continue
    if arr[i] >  arr[n-1-i]:
        res += arr[:i+1] + arr[i+1:mid+1]
        break
    else:
        res += arr[:i] + str(int(arr[i]) + 1) + arr[i+1:mid+1]
        break
 
if res == '':
    res = arr[:mid]
    res += str(int(arr[mid])+1)
if n%2 == 0:
    res += res[::-1]
else:
    res += arr[mid+1]
    res += res[-2::-1]
print(res)
