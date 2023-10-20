from itertools import combinations
for t in range(int(input())):
  n = list(input())
  temp = [i for i in range(len(n))]
  m1,m2 = int(''.join(n)), int(''.join(n))
  for value in combinations(temp,2):
    i,j = value
    n[i],n[j] = n[j],n[i]
    if n[0] == '0':
      n[i],n[j] = n[j],n[i]
      continue
    if int(''.join(n)) < m1:
      m1 = int(''.join(n))
    if int(''.join(n)) > m2:
      m2 = int(''.join(n))
    n[i],n[j] = n[j],n[i]
  print(f'#{t+1} {m1} {m2}')