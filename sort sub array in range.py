def partSort(arr, N, a, b):
    p=[] 
    # Variables to store start and 
    # end of the index range  
    l = min(a, b) 
    r = max(a, b) 
  
    # Temporary array  
    temp = [0 for i in range(r - l + 1)] 
    j = 0
    for i in range(l, r + 1, 1): 
        temp[j] = arr[i] 
        j += 1
      
    # Sort the temporary array  
    temp.sort(reverse = True) 
  
    # Modifying original array with 
    # temporary array elements  
    j = 0
    for i in range(l, r + 1, 1): 
            arr[i] = temp[j] 
            j += 1
  
    # Print the modified array  
    for i in range(0, N, 1): 
            p.append(str(arr[i]))
    return ' '.join(p)
N=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
print(partSort(arr, N, a, b))
