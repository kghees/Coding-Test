for t in range(int(input())):
  n = int(input())
  result = 0
  for _ in range(n):
    p,x = input().split()
    result += float(p)*float(x)
  print(f'#{t+1} {result:.6f}')