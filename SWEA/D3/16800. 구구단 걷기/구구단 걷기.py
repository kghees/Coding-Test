for t in range(int(input())):
  n = int(input())
  a = 1
  for i in range(2,int(n**0.5)+1):
    if n % i == 0:
      a = i
  b = n//a
  res = (a-1) + (b-1)
  print(f'#{t+1} {res}')