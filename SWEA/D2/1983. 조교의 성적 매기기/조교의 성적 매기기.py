for t in range(int(input())):
  n, k = map(int,input().split())
  score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
  num = []
  for _ in range(n):
    a,b,c = map(int,input().split())
    num.append((a*0.35) + (b*0.45) + (c*0.2))
  res = sorted(num,reverse=True)
  x = res.index(num[k-1])//(n//10)
  print(f'#{t+1} {score[x]}')