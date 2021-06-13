y,x=map(int,input().split())
arr=""
start,end=0,0
for i in range(y):
    arr+=input()
    loop=[i for i, n in enumerate(arr) if n == '=']
s=loop[0]%x
e=loop[len(loop)-1]%x
e+=1
n=0
ans=0
while(n<y):
    ans+=arr[s+x*n:e+x*n].count('O')
    n+=1
print(ans)