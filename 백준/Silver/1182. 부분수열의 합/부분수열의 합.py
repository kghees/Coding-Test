import sys
input = sys.stdin.readline
def part_sum(x):
  global cnt
  if sum(ans) == s and len(ans) > 0:
    cnt += 1
  for i in range(x, n):
    ans.append(arr[i])
    part_sum(i+1)
    ans.pop()
n, s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
ans = []
part_sum(0)
print(cnt)
