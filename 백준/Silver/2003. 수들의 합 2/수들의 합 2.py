n, m = map(int,input().split())
a = list(map(int,input().split()))
left,right = 0,1
cnt = 0
while right <= n and left <= right:
  num = sum(a[left:right])
  if num == m:
    cnt += 1
    left += 1
  elif num < m:
    right += 1
  else:
    left += 1
print(cnt)