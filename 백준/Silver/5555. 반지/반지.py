s = input()
cnt = 0
for _ in range(int(input())):
  x = input()
  if s in x:
    cnt += 1
  else:
    for i in range(10):
      if s in x[i+1:]+x[:i+1]:
        cnt += 1
        break
print(cnt)