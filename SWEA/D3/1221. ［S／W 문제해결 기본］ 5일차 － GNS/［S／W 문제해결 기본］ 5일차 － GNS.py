for t in range(int(input())):
  a, b = input().split()
  arr = list(input().split())
  num = ('ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN')
  gns = []
  for i in range(int(b)):
    gns.append(num.index(arr[i]))
  gns.sort()
  for j in range(int(b)):
    gns[j] = num[gns[j]]
  print(f'#{t+1}')
  print(*gns)