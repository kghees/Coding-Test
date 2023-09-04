n = 9
a = [int(input()) for _ in range(n)]
a.sort()
t1,t2 = 0, 0
ans = sum(a)
for i in range(n):
  for j in range(i+1,n):
    if ans - (a[i] + a[j]) == 100:
      t1 = a[i]
      t2 = a[j]
a.remove(t1)
a.remove(t2)
for i in a:
  print(i)