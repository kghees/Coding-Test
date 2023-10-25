for t in range(1,11):
  a, s = input().split()
  ans = []
  for i in s:
    if not ans:
      ans.append(i)
    elif ans and ans[-1] == i:
      ans.pop()
    else:
      ans.append(i)
  print(f'#{t}',''.join(ans))