n=int(input())
arr=""
brr=""
for x in range(n):
    if(x%2):
        arr+='C'
        brr+='.'
    else:
        arr+='.'
        brr+='C'
print((n*n+1)//2)
for x in range(n):
    if(x%2):
        print(arr)
    else:
        print(brr)