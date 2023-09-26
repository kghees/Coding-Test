def sdoku(a):
  for i in range(9):
    cnt1 = [0]*10
    cnt2 = [0]*10
    for j in range(9):
      cnt1[a[i][j]] += 1
      if cnt1[a[i][j]] >= 2:
        return 0
      cnt2[a[j][i]] += 1
      if cnt2[a[j][i]] >= 2:
        return 0
  for k in range(0,9,3):
    for l in range(0,9,3):
      cnt3 = [0]*10
      for x in range(3):
        for y in range(3):
          cnt3[a[k+x][l+y]] += 1
          if cnt3[a[k+x][l+y]] >= 2:
            return 0
  return 1
for t in range(int(input())):
  a = [list(map(int,input().split())) for _ in range(9)]
  print(f'#{t+1} {sdoku(a)}')