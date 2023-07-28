t = int(input())
for t in range(1, t+1):
  n = int(input())
  arr = [list(map(int,input())) for _ in range(n)]
  start,end = n//2, n//2
  result = 0
  for i in range(n):
    for j in range(start, end+1):
      result += arr[i][j]
    if i < n // 2:
      start -= 1
      end += 1
    else:
      start += 1
      end -= 1
  print(f'#{t} {result}')