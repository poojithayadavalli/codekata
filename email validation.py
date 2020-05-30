x=input()
count1=0
count2=0
for i in x:
    if i=='@':
        count1+=1
    if i==".":
        count2+=1
if count1 ==1 and count2==1:
    l=x[:x.index('@')]
    m=x[x.index('@')+1:x.index('.')]
    y=x[len(x)-4:len(x)]
    if(len(l)>2 and len(m)>3 and y==".com"):
        print("yes")
    else:
        print("no")
else:
    print("no")
