decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/']
for t in range(int(input())):
  s = list(input())
  ans = ''
  for i in range(len(s)):
    num = decode.index(s[i])
    bin_num = str(bin(num)[2:])

    while len(bin_num) < 6:
      bin_num = '0' + bin_num
    ans += bin_num
  
  result = ''
  for j in range(len(s)*6 // 8):
    cnt = int(ans[j*8:j*8+8],2)
    result += chr(cnt)
  print(f'#{t+1} {result}')