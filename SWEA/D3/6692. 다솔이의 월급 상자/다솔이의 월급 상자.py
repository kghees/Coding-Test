for t in range(int(input())):
  n = int(input())
  res = 0
  for _ in range(n):
    p,x = map(float,input().split())
    res += p*x
  print(f'#{t+1} {res:.6f}')