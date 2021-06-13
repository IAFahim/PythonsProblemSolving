x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    b=a*(b+1)
    a=(a//2)*b
    print(a)