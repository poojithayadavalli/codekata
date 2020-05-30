x=input()
y=input()
if x in y:
  print(list(y).index(x[0])+1)
elif y in x:
  print(list(x).index(y[0])+1)
else:
  print("-1")
