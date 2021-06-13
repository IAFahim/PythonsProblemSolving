import math
x=int(input())
arr=[int(n) for n in input().split()]
a,b,c,d=0,0,0,0
for x in arr:
    if(x==1):
        a+=1
    elif(x==2):
        b+=1
    elif(x==3):
        c+=1
    else:
        d+=1
ans=d
ans+=b//2
b%=2
if(c>=a):
    ans+=a
    ans+=b
    ans+=c-a
    #5-2
else:
    ans+=c
    a-=c
    ans+=a//4
    a%=4
    extra=a+b*2
    if(extra>0):
        if(extra<5):
            ans+=1
        else:
            ans+=2
print(ans)
