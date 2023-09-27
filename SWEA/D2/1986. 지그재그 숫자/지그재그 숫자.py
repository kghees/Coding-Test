for t in range(int(input())):
  n = int(input())
  a = [i for i in range(1, n+1)]
  result = 0
  for i in a:
    if i % 2 == 0:
      result -= i
    else:
      result += i
  print(f'#{t+1} {result}')