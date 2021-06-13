x = int(input())
for i in range(x):
    n = int(input())
    A = sorted(int(new) for new in input().split())
    B = sorted(int(new) for new in input().split())
    print(*A)
    print(*B)