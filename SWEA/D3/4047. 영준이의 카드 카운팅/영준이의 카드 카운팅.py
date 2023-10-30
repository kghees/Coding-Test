for t in range(int(input())):
  x = input()
  s,d,h,c = 13,13,13,13
  check = True
  for i in range(0,len(x),3):
    if x[i] == 'S' and x[i:i+3] not in x[i+3:]:
      s -= 1
    elif x[i] == 'D' and x[i:i+3] not in x[i+3:]:
      d -= 1
    elif x[i] == 'H' and x[i:i+3] not in x[i+3:]:
      h -= 1
    elif x[i] == 'C' and x[i:i+3] not in x[i+3:]:
      c -= 1
    else:
      check = False
      break
  if check:
    print(f'#{t+1} {s} {d} {h} {c}')
  else:
    print(f'#{t+1} ERROR')