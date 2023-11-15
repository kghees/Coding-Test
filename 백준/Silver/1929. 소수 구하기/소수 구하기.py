m,n = map(int,input().split())
num = [True]*(n+1)
num[0],num[1] = False,False
for i in range(2, int(n**0.5)+1):
  if num[i]:
    for j in range(i*2, n+1,i):
      num[j] = False
for i in range(m, n+1):
  if num[i]:
    print(i)