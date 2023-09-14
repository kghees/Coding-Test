import sys
input = sys.stdin.readline
import math
def num(x):
  if x == 0 or x == 1:
    return False
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return False
  return True
for t in range(int(input())):
  n = int(input())
  while True:
    if num(n):
      print(n)
      break
    else:
      n += 1