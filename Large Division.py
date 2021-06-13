for _ in range(int(input())):
    a,b=map(int,input().split())
    print("divisible" if a%b==0 else "not divisible")