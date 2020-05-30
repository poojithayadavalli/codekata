string = list(input())
flag=True
string1=string
for i in range(len(string)-1, 0, -1):
    if string[i] > string[i-1]:
        i = i-1
        break
    else:
        i = len(string)-1
for tmp in range(len(string)-1, i-1, -1):
    if string[tmp] > string[i]:
        string[tmp], string[i] = string[i], string[tmp]
        string = string[:i+1]+sorted(string[i+1:])
        print(''.join(string))
        flag=False
if flag:
    print(-1)
