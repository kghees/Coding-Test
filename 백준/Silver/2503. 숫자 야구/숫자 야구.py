from itertools import permutations
n = int(input())
d = ['1','2','3','4','5','6','7','8','9']
num = list(permutations(d,3))
for _ in range(n):
  a,s,b = map(int,input().split())
  a = list(str(a))
  cnt = 0
  for i in range(len(num)):
    strike,ball = 0,0
    i -= cnt
    for j in range(3):
      if num[i][j] == a[j]:
        strike += 1
      elif a[j] in num[i]:
        ball += 1
    if strike != s or ball != b:
      num.remove(num[i])
      cnt += 1
print(len(num))