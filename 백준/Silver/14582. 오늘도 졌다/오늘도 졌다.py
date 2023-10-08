a = list(map(int,input().split()))
b = list(map(int,input().split()))
x,y = 0,0
check = False
for i in range(9):
  x += a[i]
  if x > y:
    check = True
  y += b[i]
if x < y and check:
  print('Yes')
else:
  print('No')