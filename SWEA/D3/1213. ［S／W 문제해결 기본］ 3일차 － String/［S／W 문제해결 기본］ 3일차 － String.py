for t in range(1, 11):
  n = int(input())
  s = input()
  arr = input()
  cnt = 0
  for i in range(len(arr)-len(s)+1):
    if s == arr[i:len(s)+i]:
      cnt += 1
  print(f'#{t} {cnt}')