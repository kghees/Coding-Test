for t in range(int(input())):
  a,b,c,d = map(int,input().split())
  num = [0,31,59,90,120,151,181,212,243,273,304,334,365]
  result = (num[c-1]+d) - (num[a-1]+b) + 1
  print(f'#{t+1} {result}')