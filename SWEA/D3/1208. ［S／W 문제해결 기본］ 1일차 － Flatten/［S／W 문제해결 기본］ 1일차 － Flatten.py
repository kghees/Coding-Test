t = 10
for t in range(1, 11):
  n = int(input())
  dump = list(map(int,input().split()))
  dump.sort()
  for _ in range(n):
    dump[0] += 1
    dump[-1] -= 1
    dump.sort()
  print(f'#{t} {dump[-1] - dump[0]}')