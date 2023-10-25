for t in range(1,11):
  n = int(input())
  a = input()
  s = input()
  cnt = 0
  for i in range(len(s)-len(a)+1):
    if s[i:i+len(a)] == a:
      cnt += 1
  print(f'#{t} {cnt}')