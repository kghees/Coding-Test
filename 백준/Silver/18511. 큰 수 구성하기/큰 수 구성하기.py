from itertools import product
n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
b = len(str(n))
while 1:
  x = list(product(a, repeat = b))
  for i in x:
    num = int(''.join(map(str,i)))
    if num <= n:
      print(num)
      exit()
  b -= 1