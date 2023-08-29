import sys
input = sys.stdin.readline
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
arr = arr[1:]
while True:
  n = int(input())
  if n == 0:
    break
  for j in arr:
    if a[n-j] == False:
      print(f'{n} = {j} + {n-j}')
      break