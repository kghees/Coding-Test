import sys
input = sys.stdin.readline
n, p = map(int,input().split())
cnt = 0
lst = [[] for _ in range(7)]
for _ in range(n):
  l,p = map(int,input().split())
  if not lst[l-1]:
    lst[l-1].append(p)
    cnt += 1
  else:
    while lst[l-1] and lst[l-1][-1] > p:
      lst[l-1].pop()
      cnt += 1
    if not lst[l-1] or lst[l-1][-1] < p:
      lst[l-1].append(p)
      cnt += 1
    else:
      continue
print(cnt)