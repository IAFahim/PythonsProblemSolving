x=int(input())
for i in range(x):
    m=int(input())
    arr=[int(new) for new in input().split()]
    arr.sort()
    print(abs(arr[m]-arr[m-1]))