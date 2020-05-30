def sortMat(mat, m, n) : 
    # Temporary matrix of size n^2 
    temp = [0] * (m * n) 
    k = 0
  
    # Copy the elements of matrix   
    # one by one into temp[] 
    for i in range(0, m) : 
          
        for j in range(0, n) : 
              
            temp[k] = mat[i][j] 
            k += 1
  
    # sort temp[] 
    temp.sort() 
      
    # copy the elements of temp[]  
    # one by one in mat[][] 
    k = 0
      
    for i in range(0, m) : 
          
        for j in range(0, n) : 
            mat[i][j] = temp[k]
            k += 1
  
  
# Function to print the given matrix 
def printMat(mat, m, n) : 
    l=[]
    x=[]
    for i in range(0, m) :  
        for j in range( 0, n) : 
            l.append(str(mat[i][j]))
    for i in range(0,len(l),n):
        x.append(' '.join(l[i:i+n]))
    return x
m,n=map(int,input().split())
l=[]
for i in range(m):
    l.append(list(map(int,input().split())))
sortMat(l,m,n)
y=printMat(l,m,n)
for i in range(len(y)):
    print(y[i])
