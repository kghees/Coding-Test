for t in range(int(input())):
  n = int(input())
  a = list(input().split())
  shuffle = []
  if len(a) % 2 == 0:
    arr = a[:n//2]
    brr = a[n//2:]
    for i in range(n//2):
      if len(arr) > 0:
        shuffle.append(arr.pop(0))
      if len(brr) > 0:
        shuffle.append(brr.pop(0))
  else:
    arr = a[:n//2+1]
    brr = a[n//2+1:]
    for i in range(n//2+1):
      if len(arr) > 0:
        shuffle.append(arr.pop(0))
      if len(brr) > 0:
        shuffle.append(brr.pop(0))
  print(f'#{t+1}',end=' ')
  print(*shuffle)