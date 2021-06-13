n=int(input())
for n in range(n):
    x=int(input())
    if(x<2):
        print(-1)
        continue
    arr="2"
    x-=1
    for i in range(x):
           arr+="3"
    print(arr)