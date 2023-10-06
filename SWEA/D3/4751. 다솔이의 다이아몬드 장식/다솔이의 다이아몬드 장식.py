for t in range(int(input())):
  s = input()
  a = '..#.'
  b = '.#.#'
  c = '#.'
  d = '.'
  print(a*len(s)+'.')
  print(b*len(s)+'.')
  for i in s:
    print(c+i+d,end='')
  print('#')
  print(b*len(s)+'.')
  print(a*len(s)+'.')