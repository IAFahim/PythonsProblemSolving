a=int(input())
arr=[int(new) for new in input().split()]
arr.sort()
b=int(input())
brr=[int(new) for new in input().split()]
brr.sort()
print(arr[a-1],brr[b-1])