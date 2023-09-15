n = int(input())
card = [i for i in range(1, n+1)]
result = []
while len(card) > 1:
  result.append(card.pop(0))
  card.append(card.pop(0))
result.append(card.pop())
print(*result)