n=int(input())
l1=list(map(int,input().split())) 
m=int(input()) 
l2=list(map(int,input().split())) 
l=l1+l2 
l=list(set(l))
l=list(map(str,l))
print(" ".join(l))
