def factorial(n):
  x = 1
  for i in range(2, n+1):
    x = (x*i) % p
  return x
def square(x,k):
  if k == 0:
    return 1
  elif k == 1:
    return x
  temp = square(x ,k//2)
  if k % 2:
    return temp * temp * x % p
  else:
    return temp * temp % p
for t in range(int(input())):
  n, r = map(int,input().split())
  p = 1234567891
  top = factorial(n)
  bot = factorial(n-r) * factorial(r) % p
  result = top * square(bot,p-2) % p
  print(f'#{t+1} {result}')