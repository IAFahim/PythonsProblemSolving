a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
a=a-x;b=b-y;c=c-z;
frag=0
if(a>0):
    frag+=a//2;
else:
    frag+=a;
if(b>0):
    frag+=b//2;
else:
    frag+=b;
if(c>0):
    frag+=c//2;
else:
    frag+=c;
print("Yes" if frag>=0 else"No")