Y,X=map(int,input().split())
arr=[]
for y in range(Y):
    arr.append(list(input()))
eaten=0
for y in range(Y):
    for x in range(X):
        if(arr[y][x]=='W'):
            if(0<x):
                if(arr[y][x-1]=='P'):
                    eaten+=1
                    arr[y][x-1]='.'
                    continue
            if(x<X-1):
                if (arr[y][x + 1] == 'P'):
                    eaten += 1
                    arr[y][x + 1] = '.'
                    continue
            if(0<y):
                if (arr[y-1][x] == 'P'):
                    eaten += 1
                    arr[y-1][x] = '.'
                    continue
            if(y<Y-1):
                if (arr[y + 1][x] == 'P'):
                    eaten += 1
                    arr[y + 1][x] = '.'
                    continue
print(eaten)