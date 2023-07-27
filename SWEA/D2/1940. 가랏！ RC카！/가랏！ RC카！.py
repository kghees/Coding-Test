for t in range(int(input())):
  n = int(input())
  s = 0
  d = 0
  for _ in range(n):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
      s += arr[1]
    elif arr[0] == 2:
      s -= arr[1]
      if s < 0:
        s = 0
    d += s
  print(f'#{t+1} {d}')