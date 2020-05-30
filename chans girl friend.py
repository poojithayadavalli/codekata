n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(str(input()))
s1="R" 
t="R"
for i in range(m-1):
    if(t=="R"):
        s1=s1+"G"
        t="G" 
    else:
        s1=s1+"R"
        t="R"
s2="G"
t="G" 
for i in range(m-1):
    if(t=="R"):
        s2=s2+"G"
        t="G" 
    else:
        s2=s2+"R"
        t="R" 
r1=[]
r2=[] 
for i in range(n):
    c=0
    for j in range(len(l[i])):
        if(l[i][j]!=s1[j]):
            if(s1[j]=="R"):
                c=c+5 
            else:
                c=c+3 
    r1.append(c)
    c=0 
    for j in range(len(l[i])):
        if(l[i][j]!=s2[j]):
            if(s2[j]=="R"):
                c=c+5 
            else:
                c=c+3 
    r2.append(c)
sum=0 
for i in range(n):
    sum=sum+min(r1[i],r2[i])
print(sum)
