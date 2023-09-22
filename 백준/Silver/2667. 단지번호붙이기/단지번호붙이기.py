dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(a,b):
  if a < 0 or a >= n or b < 0 or b >= n:
    return False
  if d[a][b] == 1:
    global cnt
    cnt += 1
    d[a][b] = 0
    for k in range(4):
      nx = a + dx[k]
      ny = b + dy[k]
      dfs(nx,ny)
    return True
  return False 
n = int(input())
d = [list(map(int,input())) for _ in range(n)]
num = []
result = 0
cnt = 0
for i in range(n):
  for j in range(n):
    if dfs(i,j):
      num.append(cnt)
      result += 1
      cnt = 0
num.sort()
print(result)
for i in num:
  print(i)