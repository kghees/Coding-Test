left = list(input())
right = []
m = int(input())
for _ in range(m):
  arr = list(input().split())
  if left and arr[0] == 'L':
    right.append(left.pop())
  elif right and arr[0] == 'D':
    left.append(right.pop())
  elif left and arr[0] == 'B':
    left.pop()
  elif arr[0] == 'P':
    left.append(arr[1])
right.reverse()
print(''.join(left+right))