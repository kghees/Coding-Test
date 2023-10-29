for t in range(int(input())):
  n = int(input())
  a = list(map(str,input().split()))
  res = []
  if len(a) % 2 == 0:
    arr = a[:len(a)//2]
    brr = a[len(a)//2:]
    for i in range(len(a)//2):
      res.append(arr.pop(0))
      res.append(brr.pop(0))
  else:
    arr = a[:len(a)//2+1]
    brr = a[len(a)//2+1:]
    for i in range(len(a)//2):
      res.append(arr.pop(0))
      res.append(brr.pop(0))
    if arr:
      res.append(arr.pop(0))
  print(f'#{t+1}',*res)