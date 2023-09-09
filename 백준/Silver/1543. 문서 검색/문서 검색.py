a = input()
b = input()
cnt = 0
index = 0
for i in range(len(a)):
  if index > i:
    continue
  if b == a[i:i+len(b)]:
    cnt += 1
    index = i+len(b)
print(cnt)