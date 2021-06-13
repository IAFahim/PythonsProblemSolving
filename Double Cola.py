arr=["Sheldon","Leonard","Penny","Rajesh","Howard"]
x=int(input())
x-=1
while(x>=5):
    x-=5
    x//=2
print(arr[x])