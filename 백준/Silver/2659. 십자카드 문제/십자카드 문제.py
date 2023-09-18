a = list(map(int,input().split()))
def card(x):
  ans = int(''.join(map(str,x)))
  for i in range(1,4):
    temp = int(''.join(map(str,x[i:]+x[:i])))
    if ans > temp:
      ans = temp
  return ans
result = card(a)
cnt = 1
for i in range(1111, result):
  if '0' not in list(str(i)) and i == card(list(map(int,str(i)))):
    cnt += 1
print(cnt)