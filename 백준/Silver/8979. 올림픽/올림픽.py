n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[1],x[2],x[3]), reverse=True)
for i in range(n):
  if arr[i][0] == k:
    ans = i
for i in range(n):
  if arr[ans][1:] == arr[i][1:]:
    print(i+1)
    break