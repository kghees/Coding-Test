n = int(input())
a = list(map(int,input().split()))
result = [0]*n
stack = [0]
for i in range(1, n):
  if not stack:
    stack.append(i)
  while stack and a[stack[-1]] < a[i]:
    result[stack.pop()] = a[i]
  stack.append(i)
while stack:
  result[stack.pop()] = -1
for i in result:
  print(i,end=' ')