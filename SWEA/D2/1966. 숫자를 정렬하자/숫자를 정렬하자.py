for t in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  arr.sort()
  print(f'#{t+1}',end=' ')
  for i in arr:
    print(i,end=' ')
  print()