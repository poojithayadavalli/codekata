def printParenthesis(str1, n): 
    if(n > 0): 
        _printParenthesis(str1, 0,n, 0, 0) 
    return 
  
def _printParenthesis(str1, pos, n, open1, close): 
    l=[]
    if(close == n): 
        for i in str1: 
            l.append(i)
        l.append
        return ' '.join(l) 
    else: 
        if(open1 > close): 
            str1[pos] = '}' 
            _printParenthesis(str1, pos + 1, n, open1, close + 1)
        if(open1 < n): 
            str1[pos] = '{' 
            _printParenthesis(str1, pos + 1, n, open1 + 1, close) 
  
# Driver Code 
n = int(input())
str1 = [""] * 2 * n 
x=(printParenthesis(str1, n))
print(x)
#incomplete
