for t in range(int(input())):
  n, m = map(int,input().split())
  password = ['1011000', '1001100', '1100100', '1011110', '1100010', '1000110', '1111010', '1101110', '1110110', '1101000']
  result = -1
  for i in range(n):
    code = input()
    if int(code) != 0 and result == -1:
      code = str(int(code[::-1]))
    
      ans = []
      for j in range(8):
        ans.insert(0,password.index(code[j*7 : j*7+7]))
      x = (ans[0] + ans[2] + ans[4] + ans[6])*3 + ans[1] + ans[3] + ans[5] + ans[7]

      if x % 10 == 0:
        result = sum(ans)
      else:
        result = 0
  print(f'#{t+1} {result}')