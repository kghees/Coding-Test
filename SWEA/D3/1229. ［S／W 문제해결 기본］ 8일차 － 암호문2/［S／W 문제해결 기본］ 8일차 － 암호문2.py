for t in range(10):
  n = int(input())
  arr = list(map(int,input().split()))
  m = int(input())
  brr = list(input().split())
  for i in range(len(brr)):
    if brr[i] == 'I':
      a = int(brr[i+1])
      b = int(brr[i+2])
      num = list(map(int,brr[i+3:b+i+3]))
      arr[a:a] = num
    elif brr[i] == 'D':
      a = int(brr[i+1])
      b = int(brr[i+2])
      del arr[a:a+b]
  print(f'#{t+1}',end=' ')
  for i in arr[:10]:
    print(i,end=' ')
  print()