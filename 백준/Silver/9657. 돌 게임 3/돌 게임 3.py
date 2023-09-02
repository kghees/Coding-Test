n = int(input())
d = [1,1,0,1,1]
for i in range(5, n+1):
  if d[i-1] + d[i-3] + d[i-4] == 3:
    d.append(0)
  else:
    d.append(1)
if d[n] == 1:
  print('SK')
else:
  print('CY')