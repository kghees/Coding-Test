for t in range(1,11):
  n = int(input())
  arr = list(map(int,input().split()))
  m = int(input())
  brr = list(input().split())
  for i in range(len(brr)):
    if brr[i] == 'I':
      start = int(brr[i+1])
      end = int(brr[i+2])
      num = list(map(int, brr[i+3:end+i+3]))
      arr[start:start] = num
    elif brr[i] == 'D':
      start = int(brr[i+1])
      end = int(brr[i+2])
      del arr[start:start+end]
  print(f'#{t}',end=' ')
  for i in arr[:10]:
    print(i,end=' ')
  print()