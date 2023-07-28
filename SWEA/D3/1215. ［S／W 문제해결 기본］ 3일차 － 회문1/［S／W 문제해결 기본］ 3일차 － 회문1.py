for t in range(1, 11):
  n = int(input())
  arr = [list(input()) for _ in range(8)]
  cnt = 0
  for i in range(8):
    for j in range(8-n+1):
      result = 1
      for k in range(n//2):
        if arr[i][j+k] == arr[i][j+n-k-1]:
          result *= 1
        else:
          result *= 0
      if result == 1:
        cnt += 1
  for i in range(8-n+1):
    for j in range(8):
      result = 1
      for k in range(n//2):
        if arr[i+k][j] == arr[i+n-k-1][j]:
          result *= 1
        else:
          result *= 0
      if result == 1:
        cnt += 1
  print(f'#{t} {cnt}')