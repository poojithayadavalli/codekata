n=int(input())
s=input().split()
try:
    if n>=6:
        x=int(s[0])
        for i in range(1,3):
            x=x+int(s[i])
        x1=int(s[n-1])
        for i in range(n-1,n-4,-1):
            x1+=int(s[i])
        print("1" if x==x1 else "0")
except:
    print("0")
