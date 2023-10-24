for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  s = sum(a)//n
  cnt = 0
  for i in a:
    if i <= s:
      cnt += 1
  print(f'#{t+1} {cnt}')