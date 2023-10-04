for t in range(1,11):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(n)]
  cnt = 0
  for i in range(n):
    arr = []
    for j in range(n):
      if a[j][i] == 1:
        arr.append(a[j][i])
      if a[j][i] == 2 and arr:
        arr.clear()
        cnt += 1
  print(f'#{t} {cnt}')