for t in range(int(input())):
  n = int(input())
  result = 0
  for i in range(2, 65):
    a = n
    arr = []
    while a != 0:
      arr.append(a%i)
      a //= i
    if arr == arr[::-1]:
      result = 1
  print(result)