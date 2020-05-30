def getInfix(str):
    stack=[]
    for j in range(len(str)) :
        if operand(str[j]) :
            stack.append(str[j])
        else :
            operator1=stack.pop()
            operator2=stack.pop()
            stack.append( operator2 + str[j] + operator1)
    return stack.pop()        
def operand(char) :
    if (char>='a' and char<= 'z') or (char>= 'A' and char<= 'Z') : 
         return True 
    else :
        return False     
str=input()
print(getInfix(str)) 
