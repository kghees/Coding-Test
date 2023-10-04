for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  avg = sum(a)//n
  cnt = 0
  for i in range(n):
    if avg >= a[i]:
      cnt += 1
  print(f'#{t+1} {cnt}')