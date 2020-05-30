n=list(input())
l=[]
for string in n:
    if string.isupper():
        l.append(string.lower())
    elif string.islower():
        l.append(string.upper())
print(''.join(l))
