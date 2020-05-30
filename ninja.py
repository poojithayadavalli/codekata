def dif(s):
    lst=s.split()
    h=[]
    for i in range(0,len(lst)-1,2):
        m=int(lst[i+1])-int(lst[i])
        h.append(str(m))
    return' '.join(h)
s=input()
x=dif(s)
print(x)
