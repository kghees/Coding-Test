for _ in range(int(input())):
  n, m = map(int,input().split())
  a = list(map(int,input().split()))
  index = [i for i in range(n)]
  cnt = 0
  while True:
    if a[0] == max(a):
      cnt += 1
      if index[0] == m:
        print(cnt)
        break
      else:
        index.pop(0)
        a.pop(0)
    else:
      a.append(a.pop(0))
      index.append(index.pop(0))