size=int(input())
for x in range(size):
    n,k=map(int, input().split())
    sum=0
    for i in range(n):
        sum+=int(input())
    print(n-(sum//k))