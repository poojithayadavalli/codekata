def longestAlternatingSubarray(x, n): 
    longest = 1
    cnt = 1
    i = 1
    r="aeiouAEIOU"
    while i < n:
        if (x[i]in r and x[i - 1]not in r):
            cnt = cnt + 1
            longest = max(longest, cnt)
        elif (x[i]not in r and x[i-1] in r):
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
