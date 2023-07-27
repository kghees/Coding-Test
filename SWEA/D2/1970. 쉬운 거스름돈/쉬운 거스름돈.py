for t in range(int(input())):
  n = int(input())
  money = [50000,10000,5000,1000,500,100,50,10]
  arr = [0]*8
  for i in range(8):
    while 1:
      if n - money[i] >= 0:
        arr[i] += 1
        n = n - money[i]
      else:
        break
  print(f'#{t+1}')
  for i in arr:
    print(i,end=' ')
  print()