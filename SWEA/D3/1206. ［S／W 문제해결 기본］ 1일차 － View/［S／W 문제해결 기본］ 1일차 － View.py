for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  d = [-2,-1,1,2]
  cnt = 0
  for i in range(2,n-2):
    arr = []
    for k in range(4):
      arr.append(a[i+d[k]])
    arr.sort()
    if arr[-1] < a[i]:
      cnt += a[i] - arr[-1]
    else:
      continue
  print(f'#{t} {cnt}')