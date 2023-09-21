n,s,p = map(int,input().split())
if n == 0:
  print(1)
else:
  a = list(map(int,input().split()))
  if n == p and a[-1] >= s:
    print(-1)
  else:
    result = n+1
    for i in range(n):
      if a[i] <= s:
        result = i+1
        break
    print(result)