import sys
input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1],x[0]))
cnt = 0
end = 0
for a, b in arr:
  if end <= a:
    cnt += 1
    end = b
print(cnt)