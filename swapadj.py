def swap(s,i,j):
    lst=s.split()
    lst[i],lst[j]=lst[j],lst[i]
    return ' '.join(lst)
n=int(input())
s1=input()
for i in range(0,n-1,2):
    s1=swap(s1,i,i+1)
print(s1)
