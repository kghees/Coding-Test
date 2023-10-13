a = [int(input()) for _ in range(5)]
result = [0]*5
for i in range(5):
  result[i] = a.count(a[i])
x = -1
for i in range(5):
  if result[i] % 2 != 0:
    x = a[i]
    break
print(x)