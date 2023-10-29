for t in range(int(input())):
  n = int(input())
  a = [int(input()) for _ in range(n)]
  x = sum(a)//len(a)
  cnt = 0
  for i in a:
    if i > x:
      cnt += i - x
    else:
      cnt += x - i
  print(f'#{t+1} {cnt//2}')