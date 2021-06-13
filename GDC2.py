def gcd (a, b):
	if b == 0:
		return a
	else:
		return gcd (b, a % b)
x=int(input())
for x in range(x):
    arr=[int(new) for new in input().split()]
    print(gcd(arr[0],arr[1]))