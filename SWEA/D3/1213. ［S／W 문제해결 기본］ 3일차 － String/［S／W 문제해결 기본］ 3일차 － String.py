for t in range(10):
  n = int(input())
  s = input()
  string = input()
  cnt = 0
  for i in range(len(string)-len(s)+1):
    if s == string[i:i+len(s)]:
      cnt += 1
  print(f'#{t+1} {cnt}')