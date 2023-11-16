decode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for t in range(int(input())):
  s = input()
  ans = ''
  res = ''
  a = []
  for i in s:
    x = decode.index(i)
    ans += bin(x)[2:].zfill(6)
  for i in range(0,len(ans)-7,8):
    a.append(ans[i:i+8])
  for i in a:
    res += chr(int(i,2))
  print(f'#{t+1} {res}')