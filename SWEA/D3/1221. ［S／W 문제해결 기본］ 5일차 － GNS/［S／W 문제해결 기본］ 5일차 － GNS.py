num = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
for t in range(int(input())):
  s = list(input().split())
  a = list(input().split())
  res = []
  for i in range(len(a)):
    res.append(num.index(a[i]))
  res.sort()
  for i in range(len(a)):
    res[i] = num[res[i]]
  print(f'#{t+1}',*res)