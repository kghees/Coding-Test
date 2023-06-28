n = int(input())
cnt = 1
temp = True
stack = []
arr = []
for i in range(n):
  num = int(input())
  while cnt <= num:
    stack.append(cnt)
    arr.append('+')
    cnt += 1
  if stack[-1] == num:
    stack.pop()
    arr.append('-')
  else:
    temp = False
    break
if temp == False:
  print('NO')
else:
  for i in arr:
    print(i) 