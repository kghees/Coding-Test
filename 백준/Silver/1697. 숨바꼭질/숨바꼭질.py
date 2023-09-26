from collections import deque
n, k = map(int,input().split())
max = 200000
time = [-1]*(max+1)
check = [False]*(max+1)
check[n] = True
time[n] = 0
q = deque()
q.append(n)
while q:
  x = q.popleft()
  for nx in [x+1,x-1,x*2]:
    if 0 <= nx <= max and check[nx] == False:
      check[nx] = True
      time[nx] = time[x] + 1
      q.append(nx)
print(time[k])