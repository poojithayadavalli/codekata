n=input()
flag=True
for i in n:
    if i<'0' or i>'15' and (i<'A'or i>'F'):
    	flag=False
print("yes" if flag else "no")
