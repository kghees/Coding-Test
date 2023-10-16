k = 1000
num = [True]*(k+1)
num[0],num[1] = False,False
for i in range(2, int(k**0.5)+1):
  if num[i]:
    for j in range(i*2, k+1,i):
      num[j] = False
arr = []
for i in range(k+1):
  if num[i]:
    arr.append(i)
for t in range(int(input())):
  n = int(input())
  cnt = 0
  for i in range(len(arr)):
    if arr[i] < n:
      for j in range(i,len(arr)):
        if arr[j] < n:
          for k in range(j,len(arr)):
            if arr[i] + arr[j] + arr[k] == n:
              cnt += 1
  print(f'#{t+1} {cnt}')