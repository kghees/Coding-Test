#1873 상호의 배틀필드
for t in range(int(input())):
  h, w = map(int,input().split())
  data = []
  car_x, car_y = 0, 0
  car_d = ''
  for i in range(h):
    arr = list(input())
    data.append(arr)
    for j in range(len(arr)):
      if arr[j] in ['^', 'v', '<', '>']:
        car_x, car_y = i, j
        car_d = arr[j]
  n = int(input())
  nrr = list(input())
  for i in range(n):
    if nrr[i] == 'S':
      if car_d == '^':
        for j in range(car_x-1,-1,-1):
          if data[j][car_y] == '*':
            data[j][car_y] = '.'
            break
          elif data[j][car_y] == '#':
            break
      elif car_d == 'v':
        for j in range(car_x+1, h):
          if data[j][car_y] == '*':
            data[j][car_y] = '.'
            break
          elif data[j][car_y] == '#':
            break
      elif car_d == '<':
        for j in range(car_y-1,-1,-1):
          if data[car_x][j] == '*':
            data[car_x][j] = '.'
            break
          elif data[car_x][j] == '#':
            break
      elif car_d == '>':
        for j in range(car_y+1, w):
          if data[car_x][j] == '*':
            data[car_x][j] = '.'
            break
          elif data[car_x][j] == '#':
            break
    elif nrr[i] == 'U':
      car_d = '^'
      nx = car_x -1
      if nx < 0 or nx >= h:
        data[car_x][car_y] = car_d
        continue
      if data[nx][car_y] == '.':
        data[car_x][car_y] = '.'
        car_x = nx
      data[car_x][car_y] = car_d
    elif nrr[i] == 'D':
      car_d = 'v'
      nx = car_x + 1
      if nx < 0 or nx >= h:
        data[car_x][car_y] = car_d
        continue
      if data[nx][car_y] == '.':
        data[car_x][car_y] = '.'
        car_x = nx
      data[car_x][car_y] = car_d
    elif nrr[i] == 'L':
      car_d = '<'
      ny = car_y - 1
      if ny < 0 or ny >= w:
        data[car_x][car_y] = car_d
        continue
      if data[car_x][ny] == '.':
        data[car_x][car_y] = '.'
        car_y = ny
      data[car_x][car_y] = car_d
    elif nrr[i] == 'R':
      car_d = '>'
      ny = car_y + 1
      if ny < 0 or ny >= w:
        data[car_x][car_y] = car_d
        continue
      if data[car_x][ny] == '.':
        data[car_x][car_y] = '.'
        car_y = ny
      data[car_x][car_y] = car_d
  print(f'#{t+1}',end=' ')
  for i in range(h):
    print(''.join(data[i]))