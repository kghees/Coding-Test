a, p = map(int,input().split())
num = [a]
while True:
  ans = 0
  for i in str(num[-1]):
    ans += int(i)**p
  if ans in num:
    break
  num.append(ans)
print(num.index(ans))