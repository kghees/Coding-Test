for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  res = 1e9
  for i in range(7):
    if a[i] == 1:
      index = i
      x = n
      result = 0
      while x:
        if a[index] == 1:
          x -= 1
        result += 1
        index = (index+1)%7
      if res > result:
        res = result
  print(f'#{t+1} {res}')