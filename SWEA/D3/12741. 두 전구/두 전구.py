t = int(input())
res = []
for _ in range(t):
  a,b,c,d = map(int,input().split())
  num = [0]*100
  for i in range(a,b):
    num[i] += 1
  for i in range(c,d):
    num[i] += 1
  res.append(num.count(2))
for k in range(t):
  print(f'#{k+1} {res[k]}')