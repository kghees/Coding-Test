for t in range(int(input())):
  n, k = map(int,input().split())
  a = list(map(int,input().split()))
  cnt = 0
  for i in range(1, (1<<n)):
    s = 0
    for j in range(n):
      if (i & (1<<j)) > 0:
        s += a[j]
    if k == s:
      cnt += 1
  print(f'#{t+1} {cnt}')