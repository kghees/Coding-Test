def roma(x,start):
  global num
  if x == n:
    result[num] = 1
    return
  for i in range(start,4):
    num += d[i]
    roma(x+1,i)
    num -= d[i]
n = int(input())
d = [1,5,10,50]
num = 0
result = [0]*1001
roma(0,0)
print(sum(result))