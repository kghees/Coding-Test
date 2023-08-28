n = int(input())
arr = list(map(int,input().split()))
stack = []
i = 1
for _ in range(n):
  while arr:
    if arr[0] == i:
      arr.pop(0)
      i += 1
    else:
      stack.append(arr.pop(0))
    while stack:
      if stack[-1] == i:
        stack.pop()
        i += 1
      else:
        break
if not stack:
  print('Nice')
else:
  print('Sad')