def com(a,b):
  cnt = 0
  i = b
  while i <= a:
    cnt += a // i
    i *= b
  return cnt
n, m = map(int,input().split())
t,f = 0,0
t += com(n,2)
t -= com(n-m,2)
t -= com(m,2)
f += com(n,5)
f -= com(n-m,5)
f -= com(m,5)
print(min(t,f))