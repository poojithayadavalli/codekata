import sys 
  
# Recursive function to find minimum  
# number of insertions 
def findMinInsertions(str, l, h): 
  
    # Base Cases 
    if (l > h): 
        return sys.maxsize 
    if (l == h): 
        return 0
    if (l == h - 1): 
        return 0 if(str[l] == str[h]) else 1
  
    # Check if the first and last characters are 
    # same. On the basis of the comparison result,  
    # decide which subrpoblem(s) to call 
      
    if(str[l] == str[h]): 
        return findMinInsertions(str, l + 1, h - 1) 
    else: 
        return (min(findMinInsertions(str, l, h - 1), 
                    findMinInsertions(str, l + 1, h)) + 1)
x=input()
print(findMinInsertions(x,0,len(x)-1))
