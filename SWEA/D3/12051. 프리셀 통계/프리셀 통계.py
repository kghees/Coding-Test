for t in range(int(input())):
  n,d,g = map(int,input().split())
  if d != 0 and g == 0:
    print(f'#{t+1} Broken')
  elif d != 100 and g == 100:
    print(f'#{t+1} Broken')
  else:
    check = False
    for i in range(1, n+1):
      if (i*d)//100 == (i*d)/100:
        check = True
        break
    if check:
      print(f'#{t+1} Possible')
    else:
      print(f'#{t+1} Broken')