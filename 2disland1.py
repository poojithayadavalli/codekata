n=int(input())
l=[]
for i in range(n):
    l.append(input().split())
count=0
for i in range(n):
    if l[i][i+1]=="0" and l[i+1][i]=="0" and l[i+1][i+1]:
        count+=1
    elif l[i][i-1]=="0" and l[i+1][i]=="0" and l[i+1][i-1]=="0":
        count+=1
    elif l[i-1][i-1]=="0" and l[i][i-1]=="0" and l[i-1][i]=="0":
        count+=1
    elif l[i-1][i]=="0" and l[i][i+1]=="0" and l[i-1][i+1]=="0":
        count+=1
    else:
        break 
print(count)
