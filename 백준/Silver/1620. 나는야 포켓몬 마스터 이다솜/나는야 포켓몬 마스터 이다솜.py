import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = {}
for i in range(1,n+1):
  s = input().rstrip()
  arr[i] = s
  arr[s] = i
for _ in range(m):
  a = input().rstrip()
  if a.isdigit():
    print(arr[int(a)])
  else:
    print(arr[a])