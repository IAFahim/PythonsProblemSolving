import math

def lcm(a,b):
    return (a*b) // math.gcd(a,b)
a,b=map(int,input().split())
kpop=10**b
print(lcm(a,kpop))