for t in range(int(input())):
  n = int(input())
  x = 1
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      x = i
  num = n//x - 1
  x += num - 1
  print(f'#{t+1} {x}')