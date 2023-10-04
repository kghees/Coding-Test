for t in range(int(input())):
  a = list(map(int,input().split()))
  for i in range(len(a)):
    if a[i] < 40:
      a[i] = 40
  print(f'#{t+1} {sum(a)//len(a)}')