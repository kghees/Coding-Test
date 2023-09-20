n,m = map(int,input().split())
j = int(input())
start = 1
end = m
result = 0
for _ in range(j):
  t = int(input())
  if t < start:
    result += start - t
    start = t
    end = start + m - 1
  elif t > end:
    result += t - end
    end = t
    start = end - m + 1
print(result)