import sys
input = sys.stdin.readline
m, n = map(int,input().split())
nlist = [True]*(n+1)
nlist[0], nlist[1] = False, False
for i in range(2,int(n**0.5)+1):
  if nlist[i]:
    for j in range(i*2,n+1,i):
      nlist[j] = False
for i in range(m, n+1):
  if nlist[i]:
    print(i)   