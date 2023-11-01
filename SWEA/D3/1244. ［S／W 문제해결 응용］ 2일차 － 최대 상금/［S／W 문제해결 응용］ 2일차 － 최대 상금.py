def money(x,cnt):
  global res
  if cnt == int(n):
    res = max(int(''.join(a)),res)
    return
  for i in range(x,len(a)):
    for j in range(i+1,len(a)):
      if a[i] <= a[j]:
        a[i],a[j] = a[j],a[i]
        money(i,cnt+1)
        a[i],a[j] = a[j],a[i]
  if res == 0 and int(n) > cnt:
    k = (int(n) - cnt) % 2
    if k == 1:
      a[-1],a[-2] = a[-2],a[-1]
    money(x,int(n))
for t in range(int(input())):
  a, n = input().split()
  a = list(a)
  res = 0
  money(0,0)
  print(f'#{t+1} {res}')