n, m = map(int,input().split())
c = [input() for _ in range(n)]
result = []
for i in range(n-7):
  for j in range(m-7):
    cnt1, cnt2 = 0,0
    for k in range(i, i+8):
      for l in range(j, j+8):
        if (k+l) % 2 == 0:
          if c[k][l] != 'W':
            cnt1 += 1
          else:
            cnt2 += 1
        else:
          if c[k][l] != 'B':
            cnt1 += 1
          else:
            cnt2 += 1
    result.append(min(cnt1,cnt2))
print(min(result))