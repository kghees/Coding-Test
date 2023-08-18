for t in range(10):
  n = int(input())
  dump = list(map(int,input().split()))
  dump.sort()
  for i in range(n):
    dump[0] += 1
    dump[-1] -= 1
    dump.sort()
  print(f'#{t+1} {dump[-1] - dump[0]}')