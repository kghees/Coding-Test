n = int(input())
a = 1
b = n
while 1:
  mid  = (a+b)//2
  if mid**2 == n:
    print(mid)
    break
  elif mid**2 > n:
    b = mid - 1
  elif mid**2 < n:
    a = mid + 1