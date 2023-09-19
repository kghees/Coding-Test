a,b = map(int,input().split())
m = int(input())
arr = list(map(int,input().split()))
arr.reverse()
x = 0
for i in range(m):
  x += arr[i]*(a**i)
result = []
while x//b:
  result.append(x%b)
  x //= b
result.append(x)
result.reverse()
print(*result)