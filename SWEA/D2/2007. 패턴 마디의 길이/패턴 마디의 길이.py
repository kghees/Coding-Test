for t in range(int(input())):
  a = input()
  for i in range(1, 10):
    if a[:i] == a[i:2*i]:
      print(f'#{t+1} {i}')
      break