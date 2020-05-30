n=input()
for i in range(len(n)-1,-1,-1):
    if(i==len(n)-1 and n[i]=="r"):
    	print(n[i].upper(),end="")
    else:
    	print(n[i],end="")
