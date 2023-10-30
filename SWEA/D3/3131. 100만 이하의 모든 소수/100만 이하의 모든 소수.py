max = 1000000
num = [True]*(max+1)
num[0],num[1] = False,False
for i in range(2, int(max**0.5)+1):
  if num[i]:
    for j in range(i*2,max+1,i):
      num[j] = False
for i in range(max+1):
  if num[i]:
    print(i,end=' ')