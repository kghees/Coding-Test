for t in range(int(input())):
  a = list(map(int,input().split()))
  arr = []
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      for k in range(j+1,len(a)):
        x = 0
        x += a[i] + a[j] + a[k]
        if x not in arr:
          arr.append(x)
  arr.sort(reverse=True)
  print(f'#{t+1} {arr[4]}')