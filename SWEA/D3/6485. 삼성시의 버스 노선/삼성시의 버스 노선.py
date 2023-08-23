for t in range(int(input())):
  n = int(input())
  bus_stop = [0]*5001
  for i in range(n):
    a, b = map(int,input().split())
    for j in range(a, b+1):
      bus_stop[j] += 1
  print(f'#{t+1}', end=' ')
  p = int(input())
  for k in range(p):
    c = int(input())
    print(bus_stop[c],end=' ')
  print()  