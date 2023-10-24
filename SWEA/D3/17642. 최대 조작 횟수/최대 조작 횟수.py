def check(x,y):
  if x == y:
    return 0
  elif x > y:
    return -1
  elif abs(x-y) == 1:
    return -1
  elif abs(x-y) % 2 == 1:
    return (abs(x-y)-1)//2
  elif abs(x-y) % 2 == 0:
    return abs(x-y)//2
for t in range(int(input())):
  a,b = map(int,input().split())
  print(f'#{t+1} {check(a,b)}')