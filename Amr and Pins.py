import math
r,x,y,X,Y=map(int,input().split())
size=((X-x)**2+(Y-y)**2)**.5
print(math.ceil(size/(2*r)))