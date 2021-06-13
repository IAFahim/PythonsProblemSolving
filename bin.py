arr=input()
i=0
new=[]
if(arr[0]=='B'):
    new.append('W')
else:
    new.append('B')

W=int(input())
B=int(input())
found=0
while (i<len(arr)):
    no=0
    print(arr[i+1])
    if(new[i-1]=='W'and arr[i+1]=='B' and B):
        B-=1
        new.append("B")
    else:
        no+=1
    if(new[i-1]=='B'and arr[i+1]=='W' and W):
        new.append("W")
        W-=1
    else:
        no+=1
    if(no==2):
        break
    i+=1
print(new)
if(i==len(arr)):
    print("YES")
else:
    print("NO")
