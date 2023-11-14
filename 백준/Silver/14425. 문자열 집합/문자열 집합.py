n, m = map(int, input().split())
s = [input() for _ in range(n)]
cnt = 0
for _ in range(m):
    a = input()
    if a in s:
        cnt += 1
print(cnt)