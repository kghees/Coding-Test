for t in range(int(input())):
  n = int(input())
  arr = []
  for _ in range(n):
    a, b = map(int,input().split())
    brr = []
    for i in range(a, b+1):
      brr.append(i)
    arr.append(brr)
  p = int(input())
  temp = []
  for _ in range(p):
    c = int(input())
    cnt = 0
    for i in range(len(arr)):
      if c in arr[i]:
        cnt += 1
    temp.append(cnt)
  print(f'#{t+1}',end=' ')
  print(*temp) 