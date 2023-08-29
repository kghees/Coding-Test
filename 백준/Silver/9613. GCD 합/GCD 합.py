def gcd(a,b):
  while b > 0:
    a, b = b, a%b
  return a
t = int(input())
for _ in range(t):
  n = list(map(int,input().split()))
  result = 0
  for i in range(1,len(n)):
    for j in range(i+1,len(n)):
      result += gcd(n[i],n[j])
  print(result)