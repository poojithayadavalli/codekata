import math
def dist(x,y):
    xy1=(int(x[0])-int(y[0]))**2
    xy2=(int(x[1])-int(y[1]))**2
    xy=math.sqrt(xy1+xy2)
    return xy
def square(ab,ac,ad,bc,bd,cd):
    if ab==cd:
        if ac==ad and bc==bd and ac==bc:
            return True
    if ac==bd:
        if ab==ad and bc==cd and ab==bc:
            return True
    if ad==bc:
        if ab==ac and bd==cd and ab==bd:
            return True
a=input().split()
b=input().split()
c=input().split()
d=input().split()
ab=dist(a,b)
bc=dist(b,c)
cd=dist(c,d)
ad=dist(d,a)
ac=dist(a,c)
bd=dist(b,d)
print(ab)
print(ac)
print(bc)
print(ad)
print(bd)
print(cd)
if a!=b and b!=c and c!=d and d!=a and a!=c and b!=d:
    if square(ab,ac,ad,bc,bd,cd):
        print("yes")
    else:
        print("no")
