arr=list(input())
i=int("".join(arr))+1
arr=list(str(i))
while(1):
    if(arr[0]==arr[1] or arr[0]==arr[2] or arr[0]==arr[3] or arr[1]==arr[2] or arr[1]==arr[3] or arr[2]==arr[3] ):
        i=int("".join(arr))+1
        arr=list(str(i))
    else:
        break
print("".join(arr))
