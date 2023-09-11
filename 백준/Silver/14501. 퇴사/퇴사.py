n = int(input())
t = []
p = []
for i in range(n):
  a,b = map(int,input().split())
  t.append(a)
  p.append(b)
d = [0]*(n+1)
for i in range(n-1,-1,-1):
  if t[i] + i > n:
    d[i] = d[i+1]
  else:
    d[i] = max(d[i+t[i]]+p[i],d[i+1])
print(d[0])