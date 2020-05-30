n=int(input())
l=[]
for i in range(1,n):
  for j in range(n):
    if i+j==n:
      l.append(str(i)+str(j))
mini=int(l[0])
for i in range(1,len(l)):
    if int(l[i])<mini:
        mini=int(l[i])
print(mini)
