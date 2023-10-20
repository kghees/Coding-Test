for t in range(int(input())):
  n = int(input())
  s1,s2,s3 = 0,0,0
  s1 = ((1+n)*n)//2
  s2 += n**2
  s3 += (s2+n)
  print(f'#{t+1} {s1} {s2} {s3}')