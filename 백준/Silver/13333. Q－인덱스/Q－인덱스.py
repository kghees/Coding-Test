n = int(input())
a = sorted(list(map(int,input().split())))
for k in range(n,-1,-1):
  if k <= a[-k]:
    print(k)
    break