s=input().split()
x=input()
count=-1
for i in range(len(s)):
  if(x==s[i]):
    count+=1
if(count!=-1):
  print(count+1)
else:
  print(count)
