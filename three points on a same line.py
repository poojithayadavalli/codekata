def collinear(x1, y1, x2, y2, x3, y3): 
      
    """ Calculation the area of   
        triangle. We have skipped  
        multiplication with 0.5 to 
        avoid floating point computations """
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
  
    if (a == 0): 
        print("yes")
    else: 
        print("no")
l=[]
for i in range(3):
    l.append(input().split()) 
collinear(int(l[0][0]),int(l[0][1]),int(l[1][0]),int(l[1][1]),int(l[2][0]),int(l[2][1]))
