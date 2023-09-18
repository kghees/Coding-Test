def muscle(x,weight):
  global result
  if weight < 0:
    return
  if x >= n:
    result += 1
    return
  for i in range(n):
    if arr[i] == 0:
      arr[i] = 1
      muscle(x+1,weight-k+a[i])
      arr[i] = 0
n, k = map(int,input().split())
a = list(map(int,input().split()))
arr = [0]*n
result = 0
muscle(0,0)
print(result)