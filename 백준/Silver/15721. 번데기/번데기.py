a = int(input())
t = int(input())
x = int(input())
res = []
b,d = 1,1
n = 0
while 1:
  m = b
  n += 1
  for _ in range(2):
    res.append((b,0))
    b += 1
    res.append((d,1))
    d += 1
  for _ in range(n+1):
    res.append((b,0))
    b += 1
  for _ in range(n+1):
    res.append((d,1))
    d += 1
  if m < t <= b:
    print(res.index((t,x)) % a)
    break