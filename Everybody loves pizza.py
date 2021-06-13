n=int(input())
for _ in range(n):
    arr=list(input())
    M,A,R,G,I,T=0,0,0,0,0,0
    #a3 r2
    for x in arr:
        if(x=='M'):
            M+=1
        if(x=='A'):
            A+=1
        if(x=='R'):
            R+=1
        if(x=='G'):
            G+=1
        if(x=='I'):
            I+=1
        if(x=='T'):
            T+=1
    high=0
    while(M>=1 and A>=3 and R>=2 and G>=1 and I>=1 and T>=1):
            M-=1
            A-=3
            R-=2
            G-=1
            I-=1
            T-=1
            high+=1
    print(high)