def squre(n,m):
  if m > 1:
    return n*squre(n,m-1)
  else:
    return n
for _ in range(1, 11):
  t = int(input())
  n, m = map(int,input().split())
  result = squre(n,m)
  print(f'#{t} {result}')