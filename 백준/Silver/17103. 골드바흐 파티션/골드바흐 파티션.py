num = 1000000
a = [0]*(num+1)
a[0] = True
a[1] = True
arr = []
for i in range(2, num+1):
  if not a[i]:
    arr.append(i)
    j = i+i
    while j <= num:
      a[j] = True
      j += i
for _ in range(int(input())):
  n = int(input())
  cnt = 0
  for i in arr:
    if n - i >= 2 and i <= n - i:
      if a[n-i] == False:
        cnt += 1
    else:
      break
  print(cnt)