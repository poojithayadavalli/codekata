def sub(list1):
    # store all the sublists  
    sublist = [[]] 
    # first loop  
    for i in range(len(list1)+1): 
        # second loop  
        for j in range(i+1,len(list1)+1): 
            # slice the subarray  
            sub = list1[i:j] 
            sublist.append(sub) 
    return sublist 
x=input()
y=input().split()
print(len(sub(y))-1)
