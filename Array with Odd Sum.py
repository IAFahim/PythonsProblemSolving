size=int(input())
for i in range(size):
    till,sum=int(input()),0
    arr=[int(new) for new in input().split()]
    odd=0
    even=0
    for i in arr:
        sum+=i
        if(i%2):
            odd+=1
        else:
            even+=1
    if(sum%2 and sum!=1):
        print("YES")#because its already odd why fuss over it
    elif(even!=0 and odd!=0):
        print("YES")# we can switch any with NO_boino
    else:
        print("NO")#what will you swich with you are missing switching element
