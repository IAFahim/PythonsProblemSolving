def takeSecond(elem):
    return elem[1]
size=int(input())
for x in range(size):
    arr=[]
    n=int(input())
    arr=[(input().split()) for x in range(n)]
    arr.sort(key=takeSecond)
    arr.reverse()
    m=0
    m=int(arr[0][1])
    i=1
    while(i<len(arr)):
        if(m==int(arr[i][1]) and arr[i-1][0]>arr[i][0]):
            arr.pop(i-1)
        i+=1
    print(arr[0][0])
