for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  res = [1] + [0]*sum(a)
  ans = [0]
  for i in a:
    for j in range(len(ans)):
      if not res[i+ans[j]]:
        res[i+ans[j]] = 1
        ans.append(i+ans[j])
  print(f'#{t+1} {len(ans)}')