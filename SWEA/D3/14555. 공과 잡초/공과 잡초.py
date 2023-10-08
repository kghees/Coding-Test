for t in range(int(input())):
  s = input()
  print(f'#{t+1} {s.count("(") + s.count(")") - s.count("()")}')