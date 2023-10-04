for t in range(int(input())):
  s = input()
  day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
  if s == 'SUN':
    print(f'#{t+1} {7}')
  else:
    print(f'#{t+1} {7-day.index(s)-1}')