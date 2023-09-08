def go(index,first,second):
  if index == n:
    if len(first) == 0:
      return -1
    if len(second) == 0:
      return -1
    t1,t2 = 0, 0
    for i in range(len(first)):
      for j in range(len(first)):
        t1 += s[first[i]][first[j]]
    for i in range(len(second)):
      for j in range(len(second)):
        t2 += s[second[i]][second[j]]
    result = abs(t1-t2)
    return result
  ans = -1
  a = go(index+1,first+[index],second)
  if ans == -1 or (a != -1 and ans > a):
    ans = a
  b = go(index+1,first,second+[index])
  if ans == -1 or (b != -1 and ans > b):
    ans = b
  return ans
n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
print(go(0,[],[]))