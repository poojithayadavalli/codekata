x=int(input())
n=input()
print(n)
def list1(n1):
    n=list(n1)
    l=[]
    for i in range(len(n)):
        l.insert(i,max(n))
        l.append(min(n))
        n.remove(max(n))
        n.remove(min(n))
    return ' '.join(l)
y=list1(n)
print(''.join(y))
