n=int(input())
s=list(bin(n)[2:])
print(s)
count=0
for i in range(len(s)-1,-1,-1):
    count+=1
    if s[i]=='1':
        print(count)
        break        
