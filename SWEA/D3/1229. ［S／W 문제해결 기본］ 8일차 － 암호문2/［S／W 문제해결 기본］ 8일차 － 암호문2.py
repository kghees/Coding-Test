for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  m = int(input())
  s = list(input().split())
  for i in range(len(s)):
    if s[i] == 'I':
      x = int(s[i+1])
      y = int(s[i+2])
      num = list(s[i+3:i+3+y])
      a[x:x] = num
    elif s[i] == 'D':
      x = int(s[i+1])
      y = int(s[i+2])
      del a[x:x+y]
  print(f'#{t}',end=' ')
  print(*a[:10])