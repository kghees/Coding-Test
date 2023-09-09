n = int(input())
a = list(map(int,input().split()))
sigh = list(map(int,input().split()))
x = -1000000001
y = 1000000001
def dfs(num,result,plus,minus,multiply,divide):
  global x, y
  if num == n:
    x = max(x,result)
    y = min(y,result)
    return
  if plus:
    dfs(num+1,result+a[num],plus-1,minus,multiply,divide)
  if minus:
    dfs(num+1,result-a[num],plus,minus-1,multiply,divide)
  if multiply:
    dfs(num+1,result*a[num],plus,minus,multiply-1,divide)
  if divide:
    dfs(num+1,int(result/a[num]),plus,minus,multiply,divide-1)
dfs(1,a[0],sigh[0],sigh[1],sigh[2],sigh[3])
print(x)
print(y)