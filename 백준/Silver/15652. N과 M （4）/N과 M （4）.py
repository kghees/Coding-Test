n, m = map(int,input().split())
a = [0]*m
c = [False]*(n+1)
def go(index, start, n, m):
  if index == m:
    print(*a)
    return
  for i in range(start, n+1):
    a[index] = i
    go(index+1, i, n, m)
    
go(0,1,n,m)