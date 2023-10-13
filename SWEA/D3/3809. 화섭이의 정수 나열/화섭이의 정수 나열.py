for t in range(int(input())):
  n = int(input())
  ans = ''
  while True:
    ans += ''.join(map(str,input().split()))
    if len(ans) == n:
      break
  result = 0
  cnt = 0
  while True:
    if str(cnt) not in ans:
      result = cnt
      break
    cnt += 1
  print(f'#{t+1} {result}')