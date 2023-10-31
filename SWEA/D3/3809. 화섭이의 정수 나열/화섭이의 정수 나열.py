for t in range(int(input())):
  n = int(input())
  a = ''
  while True:
    a += ''.join(map(str,input().split()))
    if len(a) == n:
      break
  cnt = 0
  while True:
    if str(cnt) not in a:
      break
    cnt += 1
  print(f'#{t+1} {cnt}')