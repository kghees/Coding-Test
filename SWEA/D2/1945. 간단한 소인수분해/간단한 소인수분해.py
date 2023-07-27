for t in range(int(input())):
  n = int(input())
  num = [2,3,5,7,11]
  arr = [0]*5
  for i in range(5):
    while 1:
      if n % num[i] == 0:
        arr[i] += 1
        n = n//num[i]
      else:
        break

  print(f'#{t+1}',end=' ')
  for i in arr:
    print(i,end=' ')
  print()