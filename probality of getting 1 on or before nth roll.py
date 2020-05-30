x=int(input())
l=[]
if(x%6!=0 and x>6):
    l.append(str(x))
    l.append("6")
elif(6%x!=0 and x<6):
    l.append(str(x))
    l.append("6")
elif (x>6 and x%6==0):
    l.append(str(x//6))
    l.append(str(1))
elif (x<6 and 6%x==0):
    l.append(str(1))
    l.append(str(6//x))
print(' '.join(l))
