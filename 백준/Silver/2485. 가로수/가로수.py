import sys
from math import gcd
n = int(input())
a = int(input())
ans = []
for _ in range(n-1):
  x = int(input())
  ans.append(x-a)
  a = x
t = ans[0]
for i in range(1, len(ans)):
  t = gcd(t,ans[i])
res = 0
for k in ans:
  res += k//t - 1
print(res)