def sub_lists(list1): 
  
    # store all the sublists  
    sublist = [[]] 
    list1=[int(i)for i in list1]  
    # first loop  
    for i in range(len(list1) + 1): 
          
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
              
            # slice the subarray  
            sub = list1[i:j] 
            sublist.append(sub) 
              
      
    return sublist
x=int(input())
lst=[int(i) for i in input().split()]
y=sub_lists(lst)
sum1=sum(y[0])
for j in range(1,len(y)):
    if sum1>sum(y[j]):
        sum1=sum(y[j])
print(sum1)
