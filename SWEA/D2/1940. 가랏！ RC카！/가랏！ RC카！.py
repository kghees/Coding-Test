for t in range(int(input())):
  n = int(input())
  result = 0
  cnt = 0
  for i in range(n):
    a = list(map(int,input().split()))
    if a[0] == 1:
      cnt += a[1]
    elif a[0] == 2:
      if cnt < a[1]:
        cnt = 0
      else:
        cnt -= a[1]
    result += cnt
  print(f'#{t+1} {result}')