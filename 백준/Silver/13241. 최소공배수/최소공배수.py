import sys
input = sys.stdin.readline
a, b = map(int,input().split())
x, y = a, b
while y != 0:
  x = x % y
  x, y = y, x
print((a*b)//x)