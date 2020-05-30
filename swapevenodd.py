def swap(s,i,j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst) 
s1=input()
for i in range(0,len(s1)-1,2):
    swap(s1,i,i+1)
print(s1)
