n=input()
dic={}
count=0
for i in n:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1
for j,k in dic.items():
  if k>0 and k%3==0:
      count+=1
print(count)
#one testcase
