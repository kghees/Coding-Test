n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
for i in range(n):
    ans.append(a[i]+a[-i-1])
print(min(ans))