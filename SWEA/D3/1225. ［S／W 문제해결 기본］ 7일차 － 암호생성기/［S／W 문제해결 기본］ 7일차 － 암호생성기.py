for t in range(1, 11):
  n = int(input())
  arr = list(map(int,input().split()))
  i = 1
  while True:
    num = arr.pop(0) - i
    if num < 0:
      num = 0
      arr.append(num)
    else:
      arr.append(num)
    if num <= 0:
      break
    i += 1
    if i > 5:
      i = 1
  print(f'#{t}',end=' ')
  for i in arr:
    print(i,end=' ')
  print()