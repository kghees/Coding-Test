for t in range(int(input())):
  n = int(input())
  a,b,c,d,e = 0,0,0,0,0
  while n!=1:
    if n % 2 == 0:
      a += 1
      n /= 2
    elif n % 3 == 0:
      b += 1
      n /= 3
    elif n % 5 == 0:
      c += 1
      n /= 5
    elif n % 7 == 0:
      d += 1
      n /= 7
    elif n % 11 == 0:
      e += 1
      n /= 11
  print(f'#{t+1} {a} {b} {c} {d} {e}')