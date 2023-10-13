for t in range(int(input())):
  n = int(input())
  d = [0]*101
  d[1],d[2],d[3] = 1,1,1
  for i in range(4, 101):
    d[i] = d[i-2] + d[i-3]
  print(f'#{t+1} {d[n]}')