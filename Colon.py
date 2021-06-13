import math

A, B, H, M = map(int, input().split())

sh = math.pi * (H + M / 60) / 6

sm = math.pi * M / 30

s = abs(sh - sm)

C = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(s))

print(C)