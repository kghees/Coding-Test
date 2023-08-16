def dfs(index,count):
  global result
  if count == int(cnt):
    result = max(int(''.join(num)),result)
    return
  for i in range(index,len(num)):
    for j in range(i+1,len(num)):
      if num[i] <= num[j]:
        num[i],num[j] = num[j],num[i]
        dfs(i,count+1)
        num[i],num[j] = num[j],num[i]
  if result == 0 and int(cnt) > count:
    a = (int(cnt) - count) % 2
    if a == 1:
      num[-1],num[-2] = num[-2],num[-1]
    dfs(index,int(cnt)) 
for t in range(int(input())):
  num, cnt = input().split()
  num = list(num)
  result = 0
  dfs(0,0)
  print(f'#{t+1} {result}')