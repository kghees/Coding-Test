for t in range(int(input())):
  n = int(input())
  a = [input() for _ in range(n)]
  arr = []
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      ans = a[i]+a[j]
      if ans == ans[::-1]:
        arr.append(ans)
  for i in range(len(a)-1,-1,-1):
    for j in range(i-1,-1,-1):
      ans = a[i]+a[j]
      if ans == ans[::-1]:
        arr.append(ans)
  if arr:
    print(arr[0])
  else:
    print(0)