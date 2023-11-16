for t in range(int(input())):
  a,b,c,d = map(int,input().split())
  day = [0,31,59,90,120,151,181,212,243,273,304,334,365]
  res = (d+day[c-1]) - (b+day[a-1]) + 1
  print(f'#{t+1} {res}')