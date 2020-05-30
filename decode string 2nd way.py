def helper(s):
    res = ""
    while s:
        num = ""
        while s and s[-1] in '0123456789':
            num += s.pop()
        if num:
            num = int(num)
            s.pop()
            res += helper(s) * num
        else:
            c = s.pop()
            if c not in "[]":
                res += c
            if c == ']':
                break
    return res
def decodeString(s):
    return helper(list(s)[::-1])
x=input()
print(decodeString(x))
