import sys
input = sys.stdin.readline
t = 250000
num = [True]*(t+1)
num[0],num[1] = False,False
for i in range(2, int(t**0.5)+1):
  if num[i]:
    for j in range(i*2, t+1,i):
      num[j] = False
while True:
  n = int(input())
  if n == 0:
    break
  cnt = 0
  for i in range(n+1, 2*n+1):
    if num[i]:
      cnt += 1
  print(cnt)