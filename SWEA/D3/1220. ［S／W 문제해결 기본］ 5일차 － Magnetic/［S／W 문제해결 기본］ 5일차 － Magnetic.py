for t in range(1, 11):
  n = int(input())
  arr = [list(map(int,input().split())) for _ in range(n)]
  cnt = 0
  for i in range(n):
    ans = []
    for j in range(n):
      if arr[j][i] == 1:
        ans.append(arr[j][i])
      if arr[j][i] == 2 and ans:
        ans.clear()
        cnt += 1
  print(f'#{t} {cnt}')