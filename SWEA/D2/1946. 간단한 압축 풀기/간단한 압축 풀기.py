for t in range(int(input())):
  n = int(input())
  arr = ''
  for _ in range(n):
    x,y = input().split()
    arr += x*int(y)
  print(f'#{t+1}')
  for i in range(0,len(arr),10):
    print(arr[i:i+10])