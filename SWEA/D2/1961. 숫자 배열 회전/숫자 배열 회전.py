for t in range(int(input())):
  n = int(input())
  arr = [list(map(int,input().split())) for _ in range(n)]
  arr_90 = [[0 for _ in range(n)] for _ in range(n)]
  arr_180 = [[0 for _ in range(n)] for _ in range(n)]
  arr_270 = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      arr_90[i][j] = arr[n-j-1][i]
      arr_180[i][j] = arr[n-i-1][n-j-1]
      arr_270[i][j] = arr[j][n-i-1]
  print(f'#{t+1}')
  for x in range(n):
    for a in range(n):
      print(arr_90[x][a],end='')
    print(end=' ')
    for b in range(n):
      print(arr_180[x][b],end='')
    print(end=' ')
    for c in range(n):
      print(arr_270[x][c],end='')
    print()