for t in range(int(input())):
  n = int(input())
  res = ''
  for _ in range(n):
    a, b = input().split()
    res += a*int(b)
  print(f'#{t+1}')
  for i in range(0,len(res),10):
    print(res[i:i+10])