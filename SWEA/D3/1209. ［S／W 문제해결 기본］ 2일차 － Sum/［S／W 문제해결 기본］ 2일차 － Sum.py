for t in range(1, 11):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(100)]
  result = 0
  for i in range(100):
    if sum(a[i]) > result:
      result = sum(a[i])
  for i in range(100):
    cnt = 0
    for j in range(100):
      cnt += a[j][i]
    if result < cnt:
      result = cnt
  cnt1 = 0
  cnt2 = 0
  for i in range(100):
    cnt1 += a[i][i]
    cnt2 += a[i][99-i]
  if cnt1 > result:
    result = cnt1
  if cnt2 > result:
    result = cnt2
  print(f'#{t} {result}')