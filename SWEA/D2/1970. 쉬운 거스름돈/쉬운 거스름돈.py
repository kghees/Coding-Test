for t in range(int(input())):
  n = int(input())
  num = [50000,10000,5000,1000,500,100,50,10]
  a = [0]*8
  for i in range(8):
    while 1:
      if n - num[i] >= 0:
        a[i] += 1
        n -= num[i]
      else:
        break
  print(f'#{t+1}')
  print(*a)