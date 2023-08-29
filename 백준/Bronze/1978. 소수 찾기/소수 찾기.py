def pn(i):
  if i < 2:
    return False
  x = 2
  while x * x <= i:
    if i % x == 0:
      return False
    x += 1
  return True
n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in a:
  if pn(i):
    cnt += 1
print(cnt)