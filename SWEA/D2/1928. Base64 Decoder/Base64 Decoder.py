for t in range(int(input())):
  d ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  s = input()
  ans = ''
  arr = []
  result = ''
  for i in s:
    num = d.index(i)
    ans += bin(num)[2:].zfill(6)
  for i in range(0, len(ans)-7, 8):
    arr.append(ans[i:i+8])
  for i in arr:
    result += chr(int(i,2))
  print(f'#{t+1} {result}')