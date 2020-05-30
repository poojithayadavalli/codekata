n=input().split("B")
n=n[:len(n)-1]
print(n)
flag=1
j="ABB"
for i in range(len(n)):
    if n[i] not in j:
        flag=0
        break
print(flag)
#incomplete
