def food(x,start):
  global result
  if x == a:
   l = 1
   b = 0
   for i in arr:
    l *= i[0]
    b += i[1]
   if abs(l-b) < result:
    result = abs(l-b)
   return
  for i in range(start,n):
    arr.append(s[i])
    food(x+1,i+1)
    arr.pop()
n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
result = 1000000001
arr = []
for i in range(1, n+1):
  a = i
  food(0,0)
print(result)