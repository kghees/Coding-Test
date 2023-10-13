for t in range(int(input())):
  n = int(input())
  s = input()
  x = len(s)//2
  if s[:x] == s[x:]:
    print(f'#{t+1} Yes')
  else:
    print(f'#{t+1} No')