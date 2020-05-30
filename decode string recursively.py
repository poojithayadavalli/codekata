def decodeString(s):
    stack = []
    alphas, digits = '', ''
    for c in s:
        if c.isdigit():
            digits += c
            #print(digits)
        elif c == '[':
            stack.append((alphas, int(digits)))
            #print(stack)
            alphas, digits = '', ''
        elif c == ']':
            prev, n = stack.pop()
            #print(prev,n)
            alphas = prev + alphas* n
            #print(alphas)
        elif c.isalpha():
            alphas += c
            #print(alphas)
    return alphas
x=input()
print(decodeString(x))
