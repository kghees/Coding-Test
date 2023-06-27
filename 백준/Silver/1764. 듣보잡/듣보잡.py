n, m = map(int,input().split())
a = set()
b = set()

for _ in range(n):
  s1 = input()
  a.add(s1)

for _ in range(m):
  s2 = input()
  b.add(s2)

c = sorted(list(a & b))

print(len(c))

for i in c:
  print(i)