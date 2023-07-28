def palindrome1():
  global cnt
  for k in range(100,0,-1):
    for i in range(100):
      for j in range(100):
        if j+k > 100:
          break
        x = j + k - 1
        for l in range(j, j+(k//2)):
          if arr[i][l] != arr[i][x]:
            break
          x -= 1
        else:
          cnt = k
          return
def palindrome2():
  global cnt
  for k in range(100,0,-1):
    if cnt >= k:
      return
    for i in range(100):
      if i + k > 100:
        break
      for j in range(100):
        x = i + k - 1
        for l in range(i, i+(k//2)):
          if arr[l][j] != arr[x][j]:
            break
          x -= 1
        else:
          cnt = k
          return
for _ in range(1, 11):
  n = int(input())
  arr = [list(map(str,input())) for _ in range(100)]
  cnt = 0
  palindrome1()
  palindrome2()
  print(f'#{n} {cnt}')