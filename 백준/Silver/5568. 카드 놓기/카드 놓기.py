from itertools import permutations
import sys
n = int(input())
k = int(input())
card = [input().rstrip() for _ in range(n)]
x = set()
for i in permutations(card,k):
  x.add(''.join(i))
print(len(x))