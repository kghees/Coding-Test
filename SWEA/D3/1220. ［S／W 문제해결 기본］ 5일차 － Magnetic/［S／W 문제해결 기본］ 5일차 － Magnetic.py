for t in range(1, 11):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(n)]
  cnt = 0
  for i in range(n):
    ans = []
    for j in range(n):
      if a[j][i] == 1:
        ans.append(a[j][i])
      elif a[j][i] == 2:
        if ans and ans[-1] == 1:
          ans.clear()
          cnt += 1
  print(f'#{t} {cnt}')