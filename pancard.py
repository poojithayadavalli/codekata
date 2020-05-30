n=input()
flag=True
for i in range(len(n)):
  if(i<5 or i==len(n)-1):
    if(n[i].isupper())!=True:
      flag=False
      break
  elif(n[i].isdigit())!=True:
    flag=False
    break
print("pan" if flag else "not pan")
