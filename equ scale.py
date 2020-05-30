n=list(input())
y=list(input())
x=n.index('|')
s1=n[:x]
s2=n[x+1:]
m=0
n1=0
for i in s1:
    m+=ord(i)
for j in s2:
    n1+=ord(j)
#print(m)
#print(n)
#if m>n1:
h=n.append(y)
print(h)
#incomplete   
