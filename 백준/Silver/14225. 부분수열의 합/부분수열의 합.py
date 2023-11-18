n = int(input())
a = list(map(int,input().split()))
a.sort()
x = 0
for i in a:
  if x+1 < i:
    break
  x += i
print(x+1)