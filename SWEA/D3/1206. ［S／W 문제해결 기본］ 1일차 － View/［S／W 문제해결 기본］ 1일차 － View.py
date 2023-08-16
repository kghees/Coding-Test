for t in range(10):
  n = int(input())
  arr = list(map(int,input().split()))
  lst = [-2,-1,1,2]
  result = 0
  for i in range(2, n-2):
    x = []
    for j in lst:
      x.append(arr[i+j])
    if max(x) > arr[i]:
      continue
    else:
      result += arr[i] - max(x)
  print(f'#{t+1} {result}')