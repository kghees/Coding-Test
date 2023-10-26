for t in range(int(input())):
  s = input()
  x = '..#.'
  y = '.#.#'
  z = '#.'
  w = '.'
  print(x*len(s)+w)
  print(y*len(s)+w)
  for i in s:
    print(z+i+w,end='')
  print('#')
  print(y*len(s)+w)
  print(x*len(s)+w)