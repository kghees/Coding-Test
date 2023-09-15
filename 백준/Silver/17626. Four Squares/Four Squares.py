n = int(input())
arr = []
for i in range(n+1):
  if i**0.5 % 1:
    arr.append(0)
  else:
    arr.append(1)
m = 4
for i in range(int(n**0.5),0,-1):
  if arr[n]:
    m = 1
    break
  elif arr[n-i**2]:
    m = 2
    break
  else:
    for j in range(int((n-i**2)**0.5),0,-1):
      if arr[(n-i**2)-j**2]:
        m = 3
print(m)