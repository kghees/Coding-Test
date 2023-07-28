for t in range(1, 11):
  n = int(input())
  arr = [list(input()) for _ in range(8)]
  cnt = 0
  for i in range(8):
    for j in range(8-n+1):
      if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
        cnt += 1
  for i in range(8-n+1):
    for j in range(8):
      ans = ''
      for k in range(n):
        ans += arr[i+k][j]
      if ans == ans[::-1]:
        cnt += 1
  print(f'#{t} {cnt}')