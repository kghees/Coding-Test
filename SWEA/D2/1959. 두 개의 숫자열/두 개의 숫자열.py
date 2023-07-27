for t in range(int(input())):
  n, m = map(int,input().split())
  arr = list(map(int,input().split()))
  brr = list(map(int,input().split()))
  if n > m:
    n, m = m, n
    arr, brr = brr, arr
  result = 0
  for i in range(m-n+1):
    cnt = 0
    for j in range(n):
      cnt += arr[j] * brr[i+j]
    if cnt > result:
      result = cnt
  print(f'#{t+1} {result}')