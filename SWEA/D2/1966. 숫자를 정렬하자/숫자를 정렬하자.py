for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  a.sort()
  print(f'#{t+1}',end=' ')
  print(*a)