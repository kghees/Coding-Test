import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
print(round(sum(s)/n))
print(s[n//2])
x = Counter(s).most_common()
if len(x) > 1 and x[0][1] == x[1][1]:
  print(x[1][0])
else:
  print(x[0][0])
print(max(s)-min(s))