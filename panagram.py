s1,s2=input().split()
def pal(s):
    if s==s[::-1]:
        return True
    else:
        return False
x=sorted(s1)
y=sorted(s2)
if(pal(s1)and pal(s2)and x==y):
    print("1")
else:
    print("0")
