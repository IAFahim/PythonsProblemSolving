n=int(input())
for num in range(n):
    x=int(input())
    arr=input()
    a=1
    b=1
    for i in range(x):
        if(arr[i]=="0"):
            a*=2
        else:
            b*=3
    ans=a+b
    ans%=100003
    print(ans)