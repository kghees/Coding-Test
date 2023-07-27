for t in range(int(input())):
  arr = list(map(int,input().split()))
  arr.sort()
  cnt = sum(arr[1:9])
  result = round(cnt/8)
  print(f'#{t+1} {result}')