s=input().split()
s3=input().split()
s1=set(s3)
s2=list(s1)
s2.sort()
print(s2)
if(int(s[1])<=len(s2)):
  print(s2[int(s[1])-1])
else:
  print("-1")