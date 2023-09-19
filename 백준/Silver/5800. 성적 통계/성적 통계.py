t = int(input())
for k in range(t):
  a = list(map(int,input().split()))
  a = a[1:]
  x = max(a)
  y = min(a)
  a.sort(reverse=True)
  ans = float('-inf')
  for i in range(len(a)-1):
    temp = a[i] - a[i+1]
    if ans < temp:
      ans = temp
  print(f'Class {k+1}')
  print(f'Max {x}, Min {y}, Largest gap {ans}')