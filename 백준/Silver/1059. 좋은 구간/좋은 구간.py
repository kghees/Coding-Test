l = int(input())
s = list(map(int,input().split()))
n = int(input())
s.sort()
if n in s:
  print(0)
else:
  max_a,min_a = 0,0
  for i in s:
    if i < n:
      min_a = i
    elif n < i and max_a == 0:
      max_a = i
  max_a -= 1
  min_a += 1
  print((n-min_a)*(max_a-n+1)+(max_a-n))