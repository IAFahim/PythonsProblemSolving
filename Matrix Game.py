arr=[]
n=int(input())
for t in range(n):
    xF,yF=0,0
    y,x=map(int,input().split())
    for i in range(y):
        arr.append(input().split())
        for j in range(x):
            if(arr[i][j]=='1'):
                xF+=1
                yF+=1
    total=min(y-yF,x-xF)
    if(total&2):
        print("Vivek")
    else:
        print("Ashish")
    arr.clear()