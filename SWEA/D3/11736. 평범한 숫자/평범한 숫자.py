for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  cnt = 0
  for i in range(n-2):
    x = max(a[i],a[i+1],a[i+2])
    y = min(a[i],a[i+1],a[i+2])
    if a[i+1] != x and a[i+1] != y:
      cnt += 1
  print(f'#{t+1} {cnt}')