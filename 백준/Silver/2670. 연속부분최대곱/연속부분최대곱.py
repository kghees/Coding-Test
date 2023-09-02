n = int(input())
d = [float(input()) for _ in range(n)]
for i in range(1, n):
  d[i] = max(d[i],d[i-1]*d[i])
print('{:.3f}'.format(max(d)))