s=str(input()) 
s=list(s)
length=len(s)
f=1 
while(f>0):
    if(s[0]==s[len(s)-1]):
        s.pop(len(s)-1)
        s.pop(0)
        f+=1
    else:
        f=0  
    if(len(s)==0 or len(s)==1):
        f=0
if len(s)>0:
    print("".join(s)) 
else:
    print("Minimal string is empty")
