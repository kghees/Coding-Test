s = input()
res = []
for i in range(len(s)):
  for j in range(i,len(s)):
    res.append(s[i:j+1])
res = set(res)
print(len(res))