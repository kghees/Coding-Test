def check(x):
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  return True
for t in range(int(input())):
  n = int(input())
  for i in range(n,1000000001):
    if not check(i):
      if (i-n) > 3 and not check(i-n):
        print(f'#{t+1} {i} {i-n}')
        break