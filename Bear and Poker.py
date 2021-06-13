x=int(input())
arr=[int(new) for new in input().split()]
click="Yes"
for i in range(x):
    while(arr[i]%3==0):
        arr[i]//=3
    while(arr[i]%2==0):
        arr[i]//=2
for i in arr:
    if(arr[0]!=i):
        click="No"
        break
print(click)
