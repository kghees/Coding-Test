num = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
for t in range(int(input())):
  a,b = input().split()
  s = list(input().split())
  arr = []
  for i in range(len(s)):
    arr.append(num.index(s[i]))
  arr.sort()
  for i in range(len(arr)):
    x = int(arr[i])
    arr[i] = num[x]
  print(f'#{t+1}')
  print(*arr)