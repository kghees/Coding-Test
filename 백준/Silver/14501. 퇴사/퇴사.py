n = int(input())
t = []
p = []
d = [0 for _ in range(n+1)]
for _ in range(n):
  T, P = map(int,input().split())
  t.append(T)
  p.append(P)
for i in range(n-1,-1,-1):
  if t[i] + i > n:
    d[i] = d[i+1]
  else:
    d[i] = max(d[i+1], d[t[i]+i]+p[i])
print(d[0])