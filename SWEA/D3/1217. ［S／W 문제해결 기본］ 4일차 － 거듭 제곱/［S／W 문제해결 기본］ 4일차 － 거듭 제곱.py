def square(n,m):
  if m > 1:
    return n*square(n,m-1)
  else:
    return n
for t in range(10):
  n = int(input())
  n, m = map(int,input().split())
  result = square(n,m)
  print(f'#{t+1} {result}')