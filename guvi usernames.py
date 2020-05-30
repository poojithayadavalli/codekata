x=input()
s=input().split()
l=[]
m=[]
for i in s:
    if i in l:
      m.append(i+str(l.count(i)))
      l.append(i+str(l.count(i)))
    else:
        m.append("Verified")
        l.append(i)
print(" ".join(m))
