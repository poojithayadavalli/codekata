n=input().split()
s1=[]
for i in range(int(n[0])):
    s1.append(input().split())
r=0
s=0
for i in range(int(n[0])):
    for j in s1[i]:
        if j=="1":
            s+=1
        else:
            r+=1
print("RAM:",r)
print("SITA:",s)
#incomplete
