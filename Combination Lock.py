n=int(input())
arr=list(input())
brr=list(input())
total=0
for i in range(n):
    total+=min(10-abs(int(arr[i])-int(brr[i])),abs(int(arr[i])-int(brr[i])))
print(total)