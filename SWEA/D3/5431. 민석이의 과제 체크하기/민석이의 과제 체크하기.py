for t in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  result = []
  for i in range(1, n+1):
    if i not in a:
      result.append(i)
  print(f'#{t+1}',end=' ')
  print(*result)