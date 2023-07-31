for t in range(int(input())):
  n, a = input().split()
  s = list(input().split())
  num = ('ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN')
  new_num = []
  for i in range(int(a)):
    new_num.append(num.index(s[i]))
  new_num.sort()
  for i in range(int(a)):
    new_num[i] = num[new_num[i]]
  print(f'#{t+1}')
  print(*new_num)