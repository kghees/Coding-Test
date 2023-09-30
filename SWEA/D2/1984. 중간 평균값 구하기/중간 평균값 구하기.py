for t in range(int(input())):
  a = list(map(int,input().split()))
  a.sort()
  avg = sum(a[1:9]) / 8
  print(f'#{t+1} {round(avg)}')