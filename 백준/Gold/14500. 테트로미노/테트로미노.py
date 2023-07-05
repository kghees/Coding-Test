#테트로미노
n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
  for j in range(m):
    if j+3 < m: #1
      temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
      if ans < temp:
        ans = temp
    if i+3 < n: #2
      temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
      if ans < temp:
        ans = temp
    if i+1 < n and j+2 < m: #3
      temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
      if ans < temp:
        ans = temp
    if i+2 < n and j+1 < m:#4
      temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
      if ans < temp:
        ans = temp
    if i+1 < n and j+2 < m: #15
      temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
      if ans < temp:
        ans = temp
    if i+2 < n and j+1 < m: #14
      temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
      if ans < temp:
        ans = temp
    if i+1 < n and j+1 < m: #5
      temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
      if ans < temp:
        ans = temp
    if i-1 >= 0 and j+2 < m:#6
      temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
      if ans < temp:
        ans = temp
    if i-1 >= 0 and j+2 < m:#16
      temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
      if ans < temp:
        ans = temp
    if i+2 < n and j+1 < m:#7
      temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
      if ans < temp:
        ans = temp
    if i+2 < n and j+1 < m:#19
      temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i][j+1]
      if ans < temp:
        ans = temp
    if i+1 < n and j+2 < m:#8
      temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
      if ans < temp:
        ans = temp
    if i+1 < n and j+2 < m:#18
      temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
      if ans < temp:
        ans = temp
    if i+2 < n and j-1 >= 0:#9
      temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
      if ans < temp:
        ans = temp
    if i+2 < n and j-1 >= 0:#17
      temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1]
      if ans < temp:
        ans = temp
    if j+2 < m:
      temp = a[i][j] + a[i][j+1] + a[i][j+2]
      if i-1 >= 0:#10
        temp2 = temp + a[i-1][j+1]
        if ans < temp2:
          ans = temp2
      if i+1 < n:#11
        temp2 = temp + a[i+1][j+1]
        if ans < temp2:
          ans = temp2
    if i+2 < n:
      temp = a[i][j] + a[i+1][j] + a[i+2][j]
      if j+1 < m:#12
        temp2 = temp + a[i+1][j+1]
        if ans < temp2:
          ans = temp2
      if j-1 >= 0:#13
        temp2 = temp + a[i+1][j-1]
        if ans < temp2:
          ans = temp2
print(ans)