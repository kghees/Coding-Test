for t in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  a.sort(reverse=True)
  result = 0
  for i in range(k):
    result += a[i]
  print(f'#{t+1} {result}')