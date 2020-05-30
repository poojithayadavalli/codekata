def isOperand(c) :
    return c.isdigit()

def evaluatePrefix(exprsn) :
    Stack = []
    for i in range(len(exprsn)-1,-1,-1) :
        if isOperand(exprsn[i]) :
            Stack.append(ord(exprsn[i]) - ord('0'))
        else :
            a1 = Stack.pop()
            a2 = Stack.pop()
        if exprsn[i] == '+':
            Stack.append(a1+a2)
        elif exprsn[i] == '-':
            Stack.append(a1 - a2)
        elif exprsn[i] == '*':
            Stack.append(a1*a2)
        elif exprsn[i] == '/':
            Stack.append(a1/a2)
    return Stack[0]

s = input()
res = evaluatePrefix(s)
print(res,end='')
