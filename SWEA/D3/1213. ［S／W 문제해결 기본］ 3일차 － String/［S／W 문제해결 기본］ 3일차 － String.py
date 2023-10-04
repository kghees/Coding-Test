for t in range(1,11):
  n = int(input())
  s = input()
  x = input()
  cnt = 0
  for i in range(len(x)-len(s)+1):
    if x[i:i+len(s)] == s:
      cnt += 1
  print(f'#{t} {cnt}')