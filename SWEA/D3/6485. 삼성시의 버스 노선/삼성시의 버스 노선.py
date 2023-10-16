for t in range(int(input())):
  n = int(input())
  bus = [0]*5001
  for _ in range(n):
    a, b = map(int,input().split())
    for i in range(a, b+1):
      bus[i] += 1
  p = int(input())
  c = [int(input()) for _ in range(p)]
  print(f'#{t+1}',end=' ')
  for i in c:
    print(bus[i],end=' ')
  print()