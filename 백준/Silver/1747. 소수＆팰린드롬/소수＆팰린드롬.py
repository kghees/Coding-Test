m = 1000000
num = [True]*(m+1)
num[0],num[1] = False,False
for i in range(2, int(m**0.5)+1):
  if num[i]:
    for j in range(i*2,m+1,i):
      num[j] = False
n = int(input())
res = 0
for i in range(n, m+1):
  if i == 1:
    continue
  if str(i) == str(i)[::-1]:
    if num[i]:
      res = i
      break
if res == 0:
  res = 1003001
print(res)