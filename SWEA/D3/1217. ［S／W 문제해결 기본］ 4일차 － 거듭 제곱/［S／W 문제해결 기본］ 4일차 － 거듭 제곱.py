def squre(cnt):
  global result
  if cnt == m:
    return result
  else:
    result *= n
    squre(cnt+1)
for _ in range(1, 11):
  t = int(input())
  n, m = map(int,input().split())
  result = 1
  squre(0)
  print(f'#{t} {result}')