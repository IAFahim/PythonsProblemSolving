x=int(input())
for _ in range(x):
    n=int(input())
    arr=[int(new) for new in input().split()]
    i=1
    fix=0
    of,ef=1,0
    while(i<len(arr)):
        if(not(arr[i]%2==of and arr[i-2]%2==of)):
            fix+=1
        i+=1
    of,ef=ef,of
    print(fix)
    print(arr)