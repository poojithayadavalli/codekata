import operator
x=int(input())
y=input().split()
l=[]
freq={} 
for i in y:
    l.append(bin(int(i)))
for i in range(len(l)):
    count=0
    for j in l[i][2:]:
        if j=="1":
            count+=1
    freq[y[i]]=count
f = sorted(freq.items(), key=operator.itemgetter(1),reverse=True)
for i in f:
    print(i[0])
