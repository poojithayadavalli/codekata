def bcount(x):
    h=bin(int(x))
    count1=0
    for char in h:
        if char=="1":
            count1+=1
    return count1
n=input().split()
count=0
c1=0
for i in range(len(n)+1):
    count=bcount(n[i])
    if j in range(1,count):
        if(j%2!=0):
            c1+=1
print(c1)


