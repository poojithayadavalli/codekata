x=input().split("0")
try:
    if len(max(x))==0:
      print("-1")
    else:
        print(len(max(x)))
except:
  print("-1")
