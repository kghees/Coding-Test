d = ['.','!','?']
for t in range(int(input())):
  n = int(input())
  res = []
  cnt = 0
  i = 0
  while i < n:
    s = input().split()
    for x in s:
      x1 = x.rstrip('.?!')
      if (len(x1) == 1 and x1.isupper()) or (x1[0].isupper() and x1.isalpha() and x1[1:].islower()):
        cnt += 1
      if x[-1] in d:
        res.append(cnt)
        cnt = 0
        i += 1
  print(f'#{t+1}',*res)