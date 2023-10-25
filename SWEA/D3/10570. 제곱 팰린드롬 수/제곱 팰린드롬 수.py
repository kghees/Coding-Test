for t in range(int(input())):
  a,b = map(int,input().split())
  cnt = 0
  for i in range(a, b+1):
    if str(i) == str(i)[::-1]:
      if i**0.5 == int(i**0.5) and str(int(i**0.5)) == str(int(i**0.5))[::-1]:
        cnt += 1
  print(f'#{t+1} {cnt}')