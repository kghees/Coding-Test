for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  num = [0]*1001
  for i in range(len(a)):
    num[a[i]] += 1
  x = 0
  res = 0
  for i in range(len(num)):
    if res <= num[i]:
      res = num[i]
      x = i
  print(f'#{t+1} {x}')