n, m = map(int,input().split())
a = [0]+list(map(int,input().split()))
a.sort()
c = [False]*(n+1)
arr = [0]*m
def go(index,n,m):
  if index == m:
    print(*arr)
    return
  for i in range(1, n+1):
    if c[i]:
      continue
    arr[index] = a[i]
    c[i] = True
    go(index+1,n,m)
    c[i] = False
go(0,n,m)