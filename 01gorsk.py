n=input().split()
s=input().split()
for i in range(int(n[0])-1):
    if(int(s[i+1])-int(s[i]))>int(n[1]):
        print("1",end=" ")
    else:
        print("0",end=" ")
if(int(s[0])-int(s[len(s)-1]))>int(n[1]):
    print("1",end=" ")
else:
    print("0",end=" ")
    

    
