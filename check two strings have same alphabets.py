s1,s2 = input().split()
L1 = sorted(set(s1))
L2 = sorted(set(s2))
s3 = ''.join(L1)
s4 = ''.join(L2)
if s3==s4 :
    print('true', end='')
else :
    print('false', end='')
