for t in range(int(input())):
  n = int(input())
  result = []
  for i in range(n):
    ans = []
    for j in range(i+1):
      if j == 0 or j == i:
        ans.append(1)
      else:
        ans.append(result[i-1][j] + result[i-1][j-1])
    result.append(ans)
  print(f'#{t+1}')
  for i in result:
    print(*i)