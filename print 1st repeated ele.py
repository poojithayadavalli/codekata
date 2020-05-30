x=int(input())
y=input().split()
z=[]
flag=True
for i in y:
  if i in z:
    print(i)
    flag=True
    break
  else:
    flag=False
    z.append(i)
if flag==False:
  print("unique")
