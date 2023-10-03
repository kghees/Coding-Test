from collections import deque
n,k = map(int,input().split())
max = 200000
time = [-1]*max
check = [False]*max
q = deque()
q1 = deque()
q.append(n)
check[n] = True
time[n] = 0
while q:
  x = q.popleft()
  if x*2 < max and check[x*2] == False:
    q.append(x*2)
    check[x*2] = True
    time[x*2] = time[x]
  if x-1 >=0 and check[x-1] == False:
    q.append(x-1)
    check[x-1] = True
    time[x-1] = time[x]+1
  if x+1 < max and check[x+1] == False:
    q.append(x+1)
    check[x+1] = True
    time[x+1] = time[x]+1
  if not q:
    q = q1
    q1 = deque()
print(time[k])