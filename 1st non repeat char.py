x=input()
for i in x:
    if x.count(i)==1:
        print(i)
        flag=False
        break
    else:
        flag=True
if flag: print("-1")
