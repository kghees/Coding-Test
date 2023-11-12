import sys
input = sys.stdin.readline
k = int(input())
i = 1
res = 0
while k > 2**i:
    i += 1
x = 2**i
while k > 0:
    if k >= x:
        k -= x
    else:
        x //= 2
        res += 1
print(f'{2**i} {res}')