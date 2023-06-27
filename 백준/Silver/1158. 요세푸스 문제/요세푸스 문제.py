import sys
input = sys.stdin.readline
n, k = map(int,input().split())
arr = [i for i in range(1, n+1)]
brr = []
cnt = 0
for i in range(n):
  cnt += k-1
  if cnt >= len(arr):
    cnt = cnt % len(arr)
  
  brr.append(str(arr.pop(cnt)))
print("<",", ".join(brr)[:],">", sep='')