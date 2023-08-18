for t in range(int(input())):
  n, m = map(int,input().split())
  result = -1
  password = ['1011000','1001100','1100100','1011110','1100010','1000110','1111010','1101110','1110110','1101000']
  for i in range(n):
    code = input()
    if int(code) != 0 and result == -1:
      code = str(int(code[::-1]))
      arr = []
      for j in range(8):
        arr.insert(0,password.index(code[j*7:j*7+7]))
      d = (arr[0]+arr[2]+arr[4]+arr[6])*3 + arr[1]+arr[3]+arr[5]+arr[7]
      if d % 10 == 0:
        result = sum(arr)
      else:
        result = 0
  print(f'#{t+1} {result}')