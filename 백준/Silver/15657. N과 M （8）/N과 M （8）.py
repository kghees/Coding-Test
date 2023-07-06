n, m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
a = [0]*m
c = [False]*n
def go(index, start, n, m):
  if index == m:
    print(*a)
    return
  for i in range(start, n):
    c[i] = True
    a[index] = num[i]
    go(index+1, i, n, m)
    c[i] = False
go(0,0,n,m)