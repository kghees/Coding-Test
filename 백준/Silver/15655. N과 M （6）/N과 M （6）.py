n, m = map(int,input().split())
a = [0]+list(map(int,input().split()))
a.sort()
arr = [0]*m
def go(index,s,n,m):
  if index == m:
    print(*arr)
    return
  for i in range(s, n+1):
    arr[index] = a[i]
    go(index+1,i+1,n,m)
go(0,1,n,m)