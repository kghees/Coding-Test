n = int(input())
temp = [0]*1001
height,index,end = 0,0,0
for i in range(n):
  l, h = map(int,input().split())
  temp[l] = h
  if height < h:
    height = h
    index = l
  end = max(end,l)
stack = []
result = 0
for i in range(0, index+1):
  if not stack:
    stack.append(temp[i])
  else:
    if stack[-1] < temp[i]:
      stack.pop()
      stack.append(temp[i])
  result += stack[-1]
stack = []
for j in range(end, index, -1):
  if not stack:
    stack.append(temp[j])
  else:
    if stack[-1] < temp[j]:
      stack.pop()
      stack.append(temp[j])
  result += stack[-1]
print(result)