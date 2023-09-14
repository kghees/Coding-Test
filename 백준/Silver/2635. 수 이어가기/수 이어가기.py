n = int(input())
result = []
for i in range(1, n+1):
  first = n
  second = i
  temp = [n,i]
  while True:
    x = first - second
    if x >= 0:
      temp.append(x)
      first = second
      second = x
    else:
      if len(temp) > len(result):
        result = temp
      break
print(len(result))
print(*result)