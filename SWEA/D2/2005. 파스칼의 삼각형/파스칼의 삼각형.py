for t in range(int(input())):
  n = int(input())
  result = [[1]]
  for i in range(1, n):
    ans = [1]
    for j in range(1, i):
      ans.append(result[i-1][j-1] + result[i-1][j])
    ans.append(1)
    result.append(ans)
  print(f'#{t+1}')
  for k in result:
    print(*k,end='')
    print()