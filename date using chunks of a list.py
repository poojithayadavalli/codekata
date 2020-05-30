x=int(input())
y=input().split()
m=[]
l=[y[i:i+3]for i in range(0,len(y),3)]
for i in l:
    if int(i[2])==1987:
        if i[1]=="JANUARY" or i[1]=="MARCH" or i[1]=="MAY":
            if(int(i[0])<32):
                m.append(str(l.index(i)+1))
        elif i[1]=="JULY":
            if int(i[0])<23:
                m.append(str(l.index(i)+1))
    elif int(i[2])<1987:
        if i[1]=="JANUARY" or i[1]=="MARCH" or i[1]=="MAY"or i[1]=="JULY"or i[1]=="AUGUST"or i[1]=="OCTOBER"or i[1]=="DECEMBER":
            m.append(str(l.index(i)+1))
print(' '.join(m) if len(m) else "-1")
