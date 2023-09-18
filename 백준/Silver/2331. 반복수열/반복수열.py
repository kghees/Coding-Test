a, p = map(int,input().split())
arr = []
arr.append(a)
index = 0
while True:
  result = 0
  for i in str(arr[-1]):
    result += int(i)**p
  if result in arr:
    for j in range(len(arr)):
      if arr[j] == result:
        index = j
        break
    break
  arr.append(result)
del arr[index:]
print(len(arr))