n = int(input())
arr = []
for _ in range(n):
  a,b = map(int,input().split())
  arr.append([b,a])
arr.sort()
result = 0
for i in range(n):
  if i == 0:
    if arr[i][0] == arr[i+1][0]:
      result += (arr[i+1][1] - arr[i][1])
  elif i == n-1:
    if arr[i][0] == arr[i-1][0]:
      result += (arr[i][1] - arr[i-1][1])
  else:
    x = 1000001
    if arr[i][0] == arr[i+1][0]:
      k = (arr[i+1][1] - arr[i][1])
    if arr[i][0] == arr[i-1][0]:
      x = (arr[i][1] - arr[i-1][1])
    if x > k:
      x = k
    if x < 1000001:
      result += x
print(result)