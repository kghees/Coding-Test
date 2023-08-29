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
    if i > n:
      break
    if a[n-i] == False:
      cnt += 1
  if cnt % 2 == 0:
    cnt = cnt // 2
  else:
    cnt = cnt // 2 +1
  print(cnt)