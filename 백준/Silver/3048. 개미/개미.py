n1,n2 = map(int,input().split())
a = list(input())
b = list(input())
t = int(input())
a.reverse()
result = a + b
for _ in range(t):
  for i in range(len(result) - 1):
    if result[i] in a and result[i+1] in b:
      result[i],result[i+1] = result[i+1],result[i]
      if result[i+1] == a[-1]:
        break
print(''.join(result))