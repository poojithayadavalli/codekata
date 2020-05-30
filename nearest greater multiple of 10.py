x=input()
if int(x) in [1,2,3,4,5,6,7,8,9,10]:
  print("10")
else:
    if int(x)%10==0:
        print(int(x[:len(x)-1])*10)
    else:
        print((int(x[:len(x)-1])*10)+10)
