def next_permutation(a):
  i = len(a) - 1
  while i > 0 and a[i] <= a[i-1]:
    i -= 1
  if i <= 0:
    return False
  j = len(a) - 1
  while a[j] <= a[i-1]:
    j -= 1
  a[i-1],a[j] = a[j],a[i-1]
  j = len(a) - 1
  while i < j:
    a[i],a[j] = a[j],a[i]
    i += 1
    j -= 1
  return True
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [i for i in range(n)]
ans = 2147483647
while True:
  ok = True
  num = 0
  for i in range(0, n-1):
    if a[d[i]][d[i+1]] == 0:
      ok = False
      break
    else:
      num += a[d[i]][d[i+1]]
  if ok and a[d[-1]][d[0]] != 0:
    num += a[d[-1]][d[0]]
    ans = min(ans,num)
  if not next_permutation(d):
    break
  if d[0] != 0:
    break
print(ans)