x=int(input())
get=['x'*(x+2)]+['x'+input()+'x' for _ in range(x)]+['x'*(x+2)]#padding padding
for i in range(1,x+1):
    for j in range(1,x+1):
        each=0
        if(get[i-1][j]=='o'):
            each+=1
        if(get[i+1][j]=='o'):
            each+=1
        if(get[i][j-1]=='o'):
            each+=1
        if(get[i][j+1]=='o'):
            each+=1
        if(each%2==1):
            print("NO")
            exit()
print("YES")# not proud