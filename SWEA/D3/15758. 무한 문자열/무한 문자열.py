for t in range(int(input())):
  a, b = input().split()
  x,y = len(a),len(b)
  if a*y == b*x:
    print(f'#{t+1} yes')
  else:
    print(f'#{t+1} no')