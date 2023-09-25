t = int(input())
for k in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  ans = a[::-1]
  x = 0
  result = 0
  for i in ans:
    if x < i:
      x = i
    result += x - i
  if result > 0:
    print(f'#{k+1} {result}')
  else:
    print(f'#{k+1} {0}')