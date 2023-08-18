for t in range(int(input())):
  n = int(input())
  farm = [list(map(int,input())) for _ in range(n)]
  a, b = n//2 , n//2
  result = 0
  for i in range(n):
    for j in range(a, b+1):
      result += farm[i][j]
    if i < n//2:
      a -= 1
      b += 1
    else:
      a += 1
      b -= 1
  print(f'#{t+1} {result}')