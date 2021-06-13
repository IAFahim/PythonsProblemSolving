x=int(input())
n=x-2
arr='*'
arr+=' '*n
arr+='* '
arr+='*'*x
brr='*'
brr+=' '*n
brr+='* *'
brr+=' '*n
brr+='*'
i=0
print(arr)
while(i<n):
    print(brr)
    i=i+1
print(arr[::-1])