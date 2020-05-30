def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return ' '.join(final_list)
      
x=input()
duplicate =input().split()
print(Remove(duplicate))
