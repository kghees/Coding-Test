def good(x,y,ok):
  if ok == '<':
    if x > y:
      return False
  elif ok == '>':
    if x < y:
      return False
  return True
def go(index,num):
  if index == k+1:
    ans.append(num)
    return
  for i in range(10):
    if check[i]:
      continue
    check[i] = True
    if index == 0 or good(num[index-1],str(i),s[index-1]):
      go(index+1,num+str(i))
    check[i] = False
k = int(input())
s = input().split()
check = [False]*10
ans = []
go(0,'')
ans.sort()
print(ans[-1])
print(ans[0])