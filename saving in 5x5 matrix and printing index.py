x="WELCOMETOGUVICORPORATIONS"
y=input()
flag=True
l=[]
for i in range(0,len(x),5):
    l.append(x[i:i+5])
#print(l)
for i in l:
    if y in i:
        print(l.index(i),i.index(y[0]),sep=" ")
        print(l.index(i),i.index(y[len(y)-1]),sep=" ")
        flag=False
        break
if flag:print("0")
