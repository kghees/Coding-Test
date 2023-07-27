t = 10
for t in range(1, 11):
  n = int(input())
  building = list(map(int,input().split()))
  cnt = 0
  lst = [-1,-2,1,2]
  for i in range(2, n-2):
    x = []
    for j in lst:
      x.append(building[i+j])
    if max(x) > building[i]:
      continue
    else:
      cnt += building[i] - max(x)
  print(f'#{t} {cnt}')