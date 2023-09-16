n = int(input())
a = []
for _ in range(n):
  n,d,m,y = input().split()
  d,m,y = map(int,(d,m,y))
  a.append((y,m,d,n))
a.sort()
print(a[-1][3])
print(a[0][3])