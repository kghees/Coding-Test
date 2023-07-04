n = int(input())
a = list(map(int,input().split()))
dp = [1] * (n)
dp1 = [1] * (n)
for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      dp[i] = max(dp[i], dp[j] + 1)
a.reverse()
for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      dp1[i] = max(dp1[i],dp1[j]+1)
dp1.reverse()
dp2 = [0] * n
for i in range(n):
  dp2[i] = dp[i] + dp1[i]
print(max(dp2)-1)