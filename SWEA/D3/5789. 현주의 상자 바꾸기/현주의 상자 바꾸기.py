for t in range(int(input())):
  n,q = map(int,input().split())
  num = [0]*n
  for i in range(1,q+1):
    l,r = map(int,input().split())
    for j in range(l,r+1):
      num[j-1] = i
  print(f'#{t+1}',end=' ')
  for i in num:
    print(i,end=' ')
  print()