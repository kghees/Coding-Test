d = ['.','?','!']
for t in range(int(input())):
  n = int(input())
  res = []
  cnt = 0
  x = 0
  while x < n:
    s = input().split()
    for i in s:
      c = i.rstrip('.!?')
      if (len(c) == 1 and c.isupper()) or (c[0].isupper() and c.isalpha() and c[1:].islower()):
        cnt += 1
      if i[-1] in d:
        res.append(cnt)
        x += 1
        cnt = 0
  print(f'#{t+1}',*res)