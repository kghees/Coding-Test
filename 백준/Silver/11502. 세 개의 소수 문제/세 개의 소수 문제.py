def three(k,num):
  for i in num:
    for j in num:
      for l in num:
        if i+j+l == k:
          print(i,j,l)
          return
  print(0)
t = 1000
check = [True]*(t+1)
check[0],check[1] = False,False
for i in range(2, int(t**0.5)+1):
  if check[i]:
    for j in range(i*2,t+1,i):
      check[j] = False
num = []
for i in range(t+1):
  if check[i]:
    num.append(i)
for _ in range(int(input())):
  k = int(input())
  three(k,num)