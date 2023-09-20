v = ['a','e','i','o','u']
while True:
  s = input()
  if s == 'end':
    break
  check = True
  cnt = 0
  a, b = 0,0
  ans = ''
  for i in s:
    if i in v:
      if a == 2 or ((i != 'e' and i != 'o') and ans == i):
        check = False
        break
      else:
        a += 1
        b = 0
        cnt += 1
        ans = i
    else:
      if b == 2 or ans == i:
        check = False
        break
      else:
        b += 1
        a = 0
        ans = i
  if cnt == 0:
    check = False
  if check:
    print(f'<{s}> is acceptable.')
  else:
    print(f'<{s}> is not acceptable.')