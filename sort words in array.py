x=input()
flag=False
for i in x:
    if i in "aeiouAEIOU":
        print("yes")
        flag=True
        break
if not flag:print("no")
