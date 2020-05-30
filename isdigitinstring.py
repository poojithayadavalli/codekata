def sumdigit(s):
    sum1=0
    l=[]
    for i in s:
        if(i.isdigit()):
            sum1+=int(i)
        else:
            l.append(i)
    l.append(str(sum1))
    return ''.join(l)
n=input()
print(sumdigit(n))
