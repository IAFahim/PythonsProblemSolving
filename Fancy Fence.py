x=int(input())
for i in range(x):
    a=int(input())
    for n in range(3,400):
        ans=(n-2)*180/n
        if( ans == float(a)):
            print("YES")
            break
        elif(ans>float(a)):
            print("NO")
            break
