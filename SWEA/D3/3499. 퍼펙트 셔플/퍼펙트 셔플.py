for t in range(int(input())):
  n = int(input())
  a = list(input().split())
  arr = []
  brr = []
  stack = []
  x = 0
  if n % 2 == 0:
    x = n // 2
  else:
    x = n//2 + 1
  arr = a[:x]
  brr = a[x:]
  while True:
    if not arr:
      break
    stack.append(arr.pop(0))
    if not brr:
      break
    stack.append(brr.pop(0))
  print(f'#{t+1}',end=' ')
  print(*stack)