for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  a.sort()
  for i in range(n):
    a[-1] -= 1
    a[0] += 1
    a.sort()
  result = a[-1] - a[0]
  print(f'#{t} {result}')