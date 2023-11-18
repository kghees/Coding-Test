for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  ans = [1]+[0]*sum(a)
  res = [0]
  for i in a:
    for j in range(len(res)):
      if not ans[i+res[j]]:
        ans[i+res[j]] = 1
        res.append(i+res[j])
  print(f'#{t+1} {len(res)}')