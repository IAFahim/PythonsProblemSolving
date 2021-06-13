import statistics
s=int(input())
arr=[int(new) for new in input().split()]
arr.sort()
d=int(input())
for x in range(d):
    money=int(input())
    print(statistics.bisect_right(arr,money))