for tc in range(int(input())):
  a,b = map(int,input().split())
  def num(r1,r2,s1,s2,t1,t2):
    if r2 == 0:
      print(f'#{tc+1} {s1} {t1}')
      return
    q = r1//r2
    r = r1%r2
    s = s1 - q*s2
    t = t1 - q*t2
    return num(r2,r,s2,s,t2,t)
  num(a,b,1,0,0,1)