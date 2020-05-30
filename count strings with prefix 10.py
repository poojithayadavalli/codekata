n = int(input())
L = input().split()
s = input()
k=0
for x in L :
    if x[:len(s)]==s :
        k += 1
print(k,end='')
