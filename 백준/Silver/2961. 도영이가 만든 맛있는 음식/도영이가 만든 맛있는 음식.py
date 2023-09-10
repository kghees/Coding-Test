def food(x,y,l,b):
  global cnt
  if y != 0:
    if abs(l-b) < cnt:
      cnt = abs(l-b)
  if x == n:
    return
  food(x+1,y+1,l*s[x][0],b+s[x][1])
  food(x+1,y,l,b)
n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
cnt = 1000000001
food(0,0,1,0)
print(cnt)