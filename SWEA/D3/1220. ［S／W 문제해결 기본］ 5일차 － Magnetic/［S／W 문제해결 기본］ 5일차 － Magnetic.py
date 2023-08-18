for t in range(10):
  n = int(input())
  m = [list(map(int,input().split())) for _ in range(n)]
  cnt = 0
  for i in range(n):
    agg = []
    for j in range(n):
      if m[j][i] == 1:
        agg.append(m[j][i])
      if m[j][i] == 2 and agg:
        agg.clear()
        cnt += 1
  print(f'#{t+1} {cnt}')