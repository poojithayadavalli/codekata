def longestAlternatingSubarray(x, n): 
      
    # Length of longest alternating  
    longest = 1
    cnt = 1
  
    # Iterate in the array 
    i = 1
    while i < n:
        if (x[i]=="a" and x[i]!=x[i - 1]):
            cnt = cnt + 1
            longest = max(longest, cnt)
        elif (x[i-1]=="a"and x[i]=="b" and x[i]!=x[i - 1]):
            cnt = cnt + 1
            longest = max(longest, cnt)
        else:
            cnt = 1
        i = i + 1
    return longest  
  
# Driver Code 
a=input()
n = len(a) 
  
# Function to find the longest subarray  
print(longestAlternatingSubarray(a, n))
