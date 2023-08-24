for t in range(int(input())):
  arr = [list(map(str,input())) for _ in range(5)]
  s = [[0]*15 for _ in range(15)]
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      s[i][j] = arr[i][j]
  word = ''
  for i in range(15):
    for j in range(15):
      if s[j][i] != 0:
        word += s[j][i]
  print(f'#{t+1} {word}')