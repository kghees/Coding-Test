import sys
input = sys.stdin.readline
n, m = map(int,input().split())
s = list(map(int,input().split()))
a, b = 0, 1
cnt = 0
while b <= n and a <= b:
  num = s[a:b]
  num_sum = sum(num)

  if num_sum == m:
    cnt += 1
    b += 1
  elif num_sum < m:
    b += 1
  else:
    a += 1
print(cnt)