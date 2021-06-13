limit=10000
prime = [True] * limit
def prime_sieve():
    prime[0] = prime[1] = False
    for i, is_prime in enumerate(prime):
        if is_prime:
            yield i
            for n in range(i * i, limit, i):
                prime[n] = False
new=list(prime_sieve())
x=int(input())
mod=10**9+7
for _ in range(x):
    n=int(input())
    total=1
    for i in new:
        if(i>n):
            break
        temp=n
        count=0
        while(temp>0):
            count+=temp//i
            temp//=i
        total=((total%mod)*(count+1%mod))%mod
    print(total)