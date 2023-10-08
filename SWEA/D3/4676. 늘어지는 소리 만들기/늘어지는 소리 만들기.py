for t in range(int(input())):
  s = list(input())
  h = int(input())
  a = list(map(int,input().split()))
  a.sort(reverse=True)
  for i in a:
    s.insert(i,'-')
  print(f'#{t+1} {"".join(s)}')