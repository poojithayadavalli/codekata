def sub_lists(list1): 
  
    # store all the sublists  
    sublist = [[]] 
      
    # first loop  
    for i in range(len(list1) + 1): 
          
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
              
            # slice the subarray  
            sub = list1[i:j] 
            sublist.append(sub) 
              
      
    return sublist 
  
# driver code
n=int(input())
l1 = list(map(int,input().split()))
l2=[]
x=sub_lists(l1)
for i in range(1,len(x)):
    h=int(x[i][0])
    for j in range(len(x[i])):
        h&=int(x[i][j])
    l2.append(h)
print(max(l2))
