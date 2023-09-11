w = list(input())
answer = []
ans = []
for i in range(1, len(w)-1):
  for j in range(i+1, len(w)):
    a = w[:i]
    b = w[i:j]
    c = w[j:]
    a.reverse()
    b.reverse()
    c.reverse()
    ans.append(a+b+c)
for i in ans:
  answer.append(''.join(i))
answer.sort()
print(answer[0])