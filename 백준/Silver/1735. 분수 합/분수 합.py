import sys
input = sys.stdin.readline
a,b = map(int,input().split())
c,d = map(int,input().split())
m = a*d + c*b
n = b*d
w,z = m,n
while z > 0:
  w,z = z, w % z
m //= w
n //= w
print(m, n)