import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = {}
for i in range(n):
  s = input().split()
  arr[s[0]] = s[1]
  arr[s[1]] = s[0] 
for _ in range(m):
  a = input().rstrip()
  if a in arr:
    print(arr[a])