for t in range(10):
  c = int(input())
  arr = [list(map(int,input().split()))for _ in range(100)]
  a = 0
  for i in range(100):
    cnt = 0
    for j in range(100):
      cnt += arr[i][j]
    if cnt > a:
      a = cnt
  b = 0
  for i in range(100):
    cnt = 0
    for j in range(100):
      cnt += arr[j][i]
    if cnt > b:
      b = cnt
  c = 0
  for i in range(100):
    cnt, cnt1 = 0, 0
    cnt += arr[i][i]
    cnt1 += arr[i][99-i]
    if max(cnt,cnt1) > c:
      c = max(cnt,cnt1)
  x = max(a,b,c)
  print(f'#{t+1} {x}')