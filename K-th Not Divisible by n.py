import math
x=int(input())
for _ in range(x):
    num,th=map(int,input().split())
    print(math.floor(th+(th-1)/(num-1)))