for t in range(int(input())):
  n = int(input())
  result = 0
  ans = []
  for i in range(n):
    a,b = map(int,input().split())
    if ans:
      for x,y in ans:
        if (x > a and y < b) or (x < a and y > b):
          result += 1
    ans.append((a,b))
  print(f'#{t+1} {result}')