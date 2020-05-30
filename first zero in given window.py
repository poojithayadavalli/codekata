n=int(input())
x=list(map(int,input().split()))
k=int(input())
def printFirstNegativeInteger(arr, n, k): 
    l=[] 
    # Loop for each subarray(window) of size k 
    for i in range(0, (n - k + 1)): 
        flag = False
  
        # Traverse through the current window 
        for j in range(0, k):
            if (arr[i + j] < 0): 
          
                l.append(str(arr[i + j])) 
                flag = True
                break
        if (not(flag)): 
            l.append("0")
    return ' '.join(l)
print(printFirstNegativeInteger(x, n, k))
