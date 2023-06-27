import math
n = int(input())
s = list(map(int,input().split()))
for i in range(1,len(s)):
  gcd = math.gcd(s[0],s[i])
  a  = s[0] // gcd
  b = s[i] // gcd
  print(f"{a}/{b}")