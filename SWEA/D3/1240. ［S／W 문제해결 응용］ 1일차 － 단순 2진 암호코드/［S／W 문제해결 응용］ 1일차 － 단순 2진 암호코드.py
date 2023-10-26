for t in range(int(input())):
  n,m = map(int,input().split())
  a = [input() for _ in range(n)]
  num = ['1011000','1001100','1100100','1011110','1100010','1000110','1111010','1101110','1110110','1101000']
  res = -1
  for i in range(n):
    if int(a[i]) != 0 and res == -1:
      s = str(int(a[i][::-1]))
      ans = []
      for j in range(8):
        ans.append(num.index(s[j*7:j*7+7]))
      ans = ans[::-1]
      x = (ans[0]+ans[2]+ans[4]+ans[6])*3 + (ans[1]+ans[3]+ans[5]+ans[7])
      if x % 10 == 0:
        res = sum(ans)
      else:
        res = 0
  print(f'#{t+1} {res}')