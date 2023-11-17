for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  d = [1]*n
  for i in range(n):
    for j in range(i):
      if a[i] > a[j]:
        d[i] = max(d[i],d[j]+1)
  print(f'#{t+1} {max(d)}')