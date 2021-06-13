d=int(input())
for n in range(d):
    x=int(input())
    arr=[int(new) for new in input().split()]
    brr=""
    i=0
    while(i<x):
        if(i+2<x and arr[i]+2==arr[i+2]):
            brr+=str(arr[i]);
            brr+='...'
            i+=3
            k=i-1
            l=int(arr[k])
            while(k+1<x and arr[k]+1==arr[k+1]):
                l=int(arr[k+1]);
                k+=1;
                i=k+1;
            brr+=str(l)+','
        else:
            brr+=str(arr[i])+','
            i+=1
    brr=brr[:-1]
    print(brr)