n = int(input())
big = []
for _ in range(n):
  a, b = map(int,input().split())
  big.append((a,b))
for i in big:
  cnt = 1
  for j in big:
    if i[0] < j[0] and i[1] < j[1]:
      cnt += 1
  print(cnt, end=' ')