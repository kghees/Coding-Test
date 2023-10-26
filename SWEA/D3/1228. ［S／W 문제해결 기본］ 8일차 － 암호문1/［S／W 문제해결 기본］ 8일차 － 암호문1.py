for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  m = int(input())
  b = list(input().split())
  for i in range(len(b)):
    if b[i] == 'I':
      x = int(b[i+1])
      y = int(b[i+2])
      num = list(b[i+3:i+3+y])
      a[x:x] = num
  print(f'#{t}',*a[:10])