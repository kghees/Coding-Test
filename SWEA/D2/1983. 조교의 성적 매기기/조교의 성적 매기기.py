for t in range(int(input())):
  num = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
  n, k = map(int,input().split())
  result = []
  for _ in range(n):
    a,b,c = map(int,input().split())
    ans = result.append((a*0.35)+(b*0.45)+(c*0.2))
  x = result[k-1]
  result.sort(reverse=True)
  z = n//10
  print(f'#{t+1} {num[result.index(x)//z]}')