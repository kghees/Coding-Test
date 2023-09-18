a = input()
cnt = 0
ans = ''
while cnt < len(a):
  if a[cnt:cnt+4] == 'XXXX':
    ans += 'AAAA'
    cnt += 4
  elif a[cnt:cnt+2] == 'XX':
    ans += 'BB'
    cnt += 2
  elif a[cnt] == 'X':
    ans = -1
    break
  else:
    ans += a[cnt]
    cnt += 1
print(ans)