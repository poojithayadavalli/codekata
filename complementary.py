s=input()
l=input()
x=s+l
print(x)
flag=False
if(len(x)==26 and x.isupper()):
    for i in l:
        if i not in s:
            flag=True
print("complementary" if flag else "non-complementary")       
