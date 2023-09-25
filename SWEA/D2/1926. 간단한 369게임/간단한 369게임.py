n = int(input())
for i in range(1, n+1):
  x = str(i)
  cnt = 0
  cnt = x.count('3') + x.count('6') + x.count('9')
  if cnt != 0:
    print('-'*cnt,end=' ')
  else:
    print(x,end=' ')