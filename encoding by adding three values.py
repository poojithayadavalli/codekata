x=list(input())
for i in range(len(x)):
    if x[i]=='x':
        x[i]='a'
    elif x[i]=='y':
        x[i]='b'
    elif x[i]=='z':
        x[i]='c'
    elif x[i]=='X':
        x[i]='A'
    elif x[i]=='Y':
        x[i]='B'
    elif x[i]=='Z':
        x[i]='C'
    else:
        x[i]=chr(ord(x[i])+3)
print(''.join(x))
