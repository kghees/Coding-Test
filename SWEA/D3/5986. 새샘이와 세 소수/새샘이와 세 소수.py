max = 1000
num = [True]*max
num[0],num[1] = False,False
for i in range(2, int(max**0.5)+1):
  if num[i]:
    for j in range(i*2,max,i):
      num[j] = False
ans = []
for i in range(max):
  if num[i]:
    ans.append(i)
for t in range(int(input())):
  n = int(input())
  cnt = 0
  for i in range(len(ans)):
    if ans[i] < n:
      for j in range(i,len(ans)):
        if ans[j] < n:
          for k in range(j,len(ans)):
            if ans[i]+ans[j]+ans[k] == n:
              cnt += 1
  print(f'#{t+1} {cnt}')