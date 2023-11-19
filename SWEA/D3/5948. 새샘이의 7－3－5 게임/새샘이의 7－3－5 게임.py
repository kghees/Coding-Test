from itertools import combinations
for t in range(int(input())):
  a = list(map(int,input().split()))
  num = list(combinations(a,3))
  num.sort()
  res = []
  for i in range(len(num)):
    res.append(sum(num[i]))
  res = list(set(res))
  res.sort(reverse=True)
  print(f'#{t+1} {res[4]}')