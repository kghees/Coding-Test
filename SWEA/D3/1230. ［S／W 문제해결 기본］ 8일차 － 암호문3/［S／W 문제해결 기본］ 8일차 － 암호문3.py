for t in range(10):
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
    elif b[i] == 'D':
      x = int(b[i+1])
      y = int(b[i+2])
      del a[x:x+y]
    elif b[i] == 'A':
      x = int(b[i+1])
      a.append(b[i+2:i+2+x])
  print(f'#{t+1}',*a[:10])