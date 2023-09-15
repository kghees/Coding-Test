n = int(input())
d = [0]*n
for t in range(n):
  a = list(map(int,input().split()))
  ans = 0
  for i in range(5):
    for j in range(i+1,5):
      for k in range(j+1,5):
        result = str(a[i]+a[j]+a[k])
        if len(result) == 2:
          if ans < int(result[1]):
            ans = int(result[1])
        else:
          if ans < int(result):
            ans = int(result)
  d[t] = ans
for i in range(n-1,-1,-1):
  if d[i] == max(d):
    print(i+1)
    break