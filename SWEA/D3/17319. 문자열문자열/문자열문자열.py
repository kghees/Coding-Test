for t in range(int(input())):
  n = int(input())
  s = input()
  x = s[:len(s)//2]
  if x*2 == s:
    print(f'#{t+1} Yes')
  else:
    print(f'#{t+1} No')