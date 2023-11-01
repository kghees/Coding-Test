max = 1000000
num = [True]*(max+1)
num[0],num[1] = False,False
for i in range(2, int(max**0.5)+1):
  if num[i]:
    for j in range(i*2,max+1,i):
      num[j] = False
for t in range(int(input())):
  d,a,b = map(int,input().split())
  cnt = 0
  for i in range(a, b+1):
    if num[i]:
      if str(d) in str(i):
        cnt += 1
  print(f'#{t+1} {cnt}')