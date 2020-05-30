s = 'I am john cena cena john'
L = input().split()
i=0
while True :
    if i >= len(L)-1 :
        break
    if L[i] == L[i+1] :
        x = L[i]
        L.remove(x)
        L.remove(x)
        i = 0
    else :
        i += 1
print(*L,end='')
