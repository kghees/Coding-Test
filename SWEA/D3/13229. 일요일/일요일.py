for t in range(int(input())):
  s = input()
  day = ['0','MON','TUE','WED','THU','FRI','SAT','SUN']
  x = day.index(s)
  if x == 7:
    print(f'#{t+1} 7')
  else:
    print(f'#{t+1} {7-x}')