x=int(input())
n=list(map(int,input().split()))
def list1(n):
    l=[]
    if x%2==0:
        y=x//2
    else:
        y=x//2+1
    for i in range(y):
        if max(n)!=min(n):
            l.append(max(n))
            l.append(min(n))
            n.remove(max(n))
            n.remove(min(n))
        else:
            l.append(max(n))
            n.remove(max(n))
    m=list(map(str,l))
    return ' '.join(m)
print(list1(n))
