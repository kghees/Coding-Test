n = input()
sum = 0
for i in range(len(n)-1):
  sum += 9 * 10 ** i * (i+1)
sum += (int(n) - 10 ** (len(n)-1)+1) * len(n)
print(sum)