def change(num):
  if s[num] == 0:
    s[num] = 1
  else:
    s[num] = 0
  return
n = int(input())
s = [-1] + list(map(int,input().split()))
for _ in range(int(input())):
  a, b = map(int,input().split())
  if a == 1:
    for i in range(b,n+1,b):
      change(i)
  if a == 2:
    change(b)
    for k in range(n//2):
      if b + k > n or b - k <= 0:
        break
      if s[b+k] == s[b-k]:
        change(b+k)
        change(b-k)
      else:
        break
for i in range(1, n+1):
  print(s[i],end=' ')
  if i % 20 == 0:
    print()