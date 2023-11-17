d = ['N','E','S','W']
res = 'N'
for i in range(10):
  n = int(input())
  if n == 1:
    res = d[(d.index(res)+1)%4]
  elif n == 2:
    res = d[(d.index(res)+2)%4]
  elif n == 3:
    res = d[(d.index(res)+3)%4]
print(res)