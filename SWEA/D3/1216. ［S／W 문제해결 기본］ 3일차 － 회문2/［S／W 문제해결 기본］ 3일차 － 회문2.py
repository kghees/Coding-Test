def check():
  global cnt
  for k in range(100,0,-1):
    for i in range(100):
      for j in range(100):
        if j + k > 100:
          break
        x = j+k-1
        for l in range(j,j+k//2):
          if a[i][x] != a[i][l]:
            break
          x -= 1
        else:
          cnt = k
          return
def check1():
  global cnt
  for k in range(100,0,-1):
    if cnt >= k:
      return
    for i in range(100):
      for j in range(100):
        if i + k > 100:
          break
        x = i+k-1
        for l in range(i, i+k//2):
          if a[x][j] != a[l][j]:
            break
          x -= 1
        else:
          cnt = k
          return
for t in range(1,11):
  n = int(input())
  a = [list(input()) for _ in range(100)]
  cnt = 0
  check()
  check1()
  print(f'#{t} {cnt}')