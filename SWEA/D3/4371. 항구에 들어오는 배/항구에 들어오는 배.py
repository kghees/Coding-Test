for t in range(int(input())):
  n = int(input())
  a = [int(input()) for _ in range(n)]
  ans = []
  cnt = 0
  for i in range(1, len(a)):
    if a[i] in ans:
      continue
    x = a[i]-1
    for j in range(x+1,a[-1]+1,x):
      ans.append(j)
    cnt += 1
  print(f'#{t+1} {cnt}')