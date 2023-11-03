def check(a,b):
  if a == b:
    return 0
  elif a > b:
    return -1
  elif b-a == 1:
    return -1
  elif (b-a) % 2 == 1:
    return ((b-a)-1)//2
  elif (b-a) % 2 == 0:
    return (b-a)//2
for t in range(int(input())):
  a,b = map(int,input().split())
  print(f'#{t+1} {check(a,b)}')