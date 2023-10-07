for t in range(int(input())):
  n,m = map(int,input().split())
  result = -1
  num = ['1011000','1001100','1100100','1011110','1100010','1000110','1111010','1101110','1110110','1101000']
  for i in range(n):
    s = input()
    if int(s) != 0 and result == -1:
      ans = str(int(s[::-1]))
      arr = []
      for k in range(8):
        arr.insert(0,num.index(ans[k*7:k*7+7]))
      x = (arr[0]+arr[2]+arr[4]+arr[6])*3 + (arr[1]+arr[3]+arr[5]+arr[7])
      if x % 10 == 0:
        result = sum(arr)
      else:
        result = 0
  print(f'#{t+1} {result}')