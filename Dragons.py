s,n=map(int,input().split())
pair=[]
for i in range(n):
    h,b=map(int,input().split())
    pair.append((h,b))
pair.sort()
for i in range(n):
    if(not(s>pair[i][0])):
        print("NO")
        break
    else:
        if(n==i+1):
            print("YES")
            break
        s+=pair[i][1];
