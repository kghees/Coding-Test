for t in range(int(input())):
  n,d = map(int,input().split())
  if n % (d*2+1) == 0:
    print(f'#{t+1} {n//(d*2+1)}')
  else:
    print(f'#{t+1} {n//(d*2+1)+1}')