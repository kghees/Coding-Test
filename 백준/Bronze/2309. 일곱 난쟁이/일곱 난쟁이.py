a = []
for _ in range(9):
  a.append(int(input()))
result = sum(a)
a.sort()
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if result - a[i] - a[j] == 100:
      for k in range(len(a)):
        if i == k or j == k:
          continue
        else:
          print(a[k])
      exit()
      