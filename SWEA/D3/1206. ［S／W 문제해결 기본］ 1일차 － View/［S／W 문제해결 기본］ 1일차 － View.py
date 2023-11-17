for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  res = 0
  num = [-2,-1,1,2]
  for i in range(2, len(a)-2):
    ans = []
    for k in range(4):
      if a[i] < a[i+num[k]]:
        break
      else:
        ans.append(a[i+num[k]])
    if len(ans) == 4:
      res += a[i] - max(ans)
  print(f'#{t} {res}')