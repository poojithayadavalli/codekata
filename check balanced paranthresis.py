s=str(input())
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
for i in range(0,len(s)):
  if(s[i]=="{"):
    c1=c1+1
  elif(s[i]=="}"):
    c2=c2+1
  elif(s[i]=="["):
    c3=c3+1
  elif(s[i]=="]"):
    c4=c4+1
  elif(s[i]=="("):
    c5=c5+1
  elif(s[i]==")"):
    c6=c6+1 
if(c1==c2 and c3==c4 and c5==c6):
  print("yes")
else:
  print("no")
