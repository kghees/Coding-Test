def dfs(start,ans,x):
  global cnt
  if len(ans) == x:
    num = [0]*26
    for i in ans:
      for j in i:
        j = j.lower()
        if 0 <= ord(j) - 97 < 26:
          num[ord(j) - ord('a')] = 1
    if sum(num) == 26:
      cnt += 1
    return
  for i in range(start,n):
    if check[i] == False:
      check[i] = True
      ans.append(a[i])
      dfs(i+1,ans,x)
      ans.pop()
      check[i] = False
for t in range(int(input())):
  n = int(input())
  a = [input() for _ in range(n)]
  e = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  cnt = 0
  check = [False]*n
  for x in range(1, n+1):
    dfs(0,[],x)
  print(f'#{t+1} {cnt}')