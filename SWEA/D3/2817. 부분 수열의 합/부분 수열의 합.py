def part_sum(x):
  global res
  if sum(ans) == k:
    res += 1
  for i in range(x,n):
    ans.append(a[i])
    part_sum(i+1)
    ans.pop()
for t in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  res = 0
  ans = []
  part_sum(0)
  print(f'#{t+1} {res}')