hel="hello"
arr=input()
i=0
for x in range(len(arr)):
    if(hel[i]==arr[x]):
        i+=1
    if(i==5):
        print("YES")
        exit()
print("NO")