n = int(input())
d = [0,1]
for i in range(2, n+1):
  x = 4
  j = 1
  while j*j <= i:
    x = min(x,d[i-j*j])
    j += 1
  d.append(x+1)
print(d[n])