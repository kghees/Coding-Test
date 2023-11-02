for t in range(int(input())):
  a,b = input().split()
  if a*len(b) == b*len(a):
    print(f'#{t+1} yes')
  else:
    print(f'#{t+1} no')