for t in range(int(input())):
  a,b,c = map(int,input().split())
  if a == b:
    print(f'#{t+1} {c}')
  elif b == c:
    print(f'#{t+1} {a}')
  elif a == c:
    print(f'#{t+1} {b}')
  else:
    print(f'#{t+1} {a}')