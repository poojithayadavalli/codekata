def maxOfSegmentMins(a,n,k): 
  
    # if we have to divide it into 1 segment  
    # then the min will be the answer  
    if k ==1: 
        return min(a) 
    if k==2: 
        return max(a[0],a[n-1]) 
  
    # If k >= 3, return maximum of all  
    #  elements.  
    return max(a) 

n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(maxOfSegmentMins(arr,n,k))
