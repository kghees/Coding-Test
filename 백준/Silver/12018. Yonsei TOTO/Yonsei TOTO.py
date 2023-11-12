n, m = map(int, input().split())
res = 0
ans = []
for _ in range(n):
    p, l = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if p >= l:
        ans.append(a[l-1])
    else:
        ans.append(1)
ans.sort()
for i in ans:
    if m >= i:
        res += 1
        m -= i
print(res)