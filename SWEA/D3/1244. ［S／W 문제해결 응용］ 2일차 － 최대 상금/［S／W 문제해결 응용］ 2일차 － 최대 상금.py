def money(x,cnt):
  global result
  if int(c) == cnt:
    result = max(int(''.join(n)),result)
    return
  for i in range(x,len(n)):
    for j in range(i+1,len(n)):
      if n[i] <= n[j]:
        n[i],n[j] = n[j],n[i]
        money(i,cnt+1)
        n[i],n[j] = n[j],n[i]
  if result == 0 and int(c) > cnt:
    a = (int(c) - cnt) % 2
    if a == 1:
      n[-1],n[-2] = n[-2],n[-1]
    money(x,int(c))    
for t in range(int(input())):
  n, c = input().split()
  n = list(n)
  result = 0
  money(0,0)
  print(f'#{t+1} {result}')