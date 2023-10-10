for t in range(int(input())):
  n = int(input())
  a = [int(input()) for _ in range(n)]
  avg = sum(a) // len(a)
  result = 0
  for i in a:
    if i < avg:
      result += abs(avg-i)
  print(f'#{t+1} {result}')