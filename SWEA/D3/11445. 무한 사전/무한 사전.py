for t in range(int(input())):
  p = input().rstrip()
  q = input().rstrip()
  
  p += 'a'
  if p == q:
    print(f'#{t+1} N')
  else:
    print(f'#{t+1} Y')