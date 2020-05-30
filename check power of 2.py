x=int(input())
flag=False
for i in range(1,x//2):
    if x==(2**i):
        flag=True
        break
if flag:
    print("yes")
else:
    print("no")
