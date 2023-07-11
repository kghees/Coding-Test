k = int(input())
a = [0]*(k+1)
b = [0]*(k+1)
a[1] = 0
b[1] = 1
for i in range(2,k+1):
  if i == 2:
    a[2] = 1
    b[2] = 1
  else:
    a[i] = a[i-1] + a[i-2]
    b[i] = b[i-1] + b[i-2]
print(a[k],b[k])