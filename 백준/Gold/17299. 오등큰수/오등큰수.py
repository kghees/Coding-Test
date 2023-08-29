n = int(input())
a = list(map(int,input().split()))
count = [0]*1000001
result = [0]*n
stack = [0]
for i in range(n):
  count[a[i]] += 1
for i in range(1, n):
  if not stack:
    stack.append(i)
  else:
    while stack and count[a[stack[-1]]] < count[a[i]]:
      result[stack.pop()] = a[i]
    stack.append(i)
while stack:
  result[stack.pop()] = -1
for i in result:
  print(i,end=' ')