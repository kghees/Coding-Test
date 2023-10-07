import sys
input = sys.stdin.readline
k,l = map(int,input().split())
dict = {}
for i in range(l):
  dict[input().rstrip()] = i
result = sorted(dict.items(),key = lambda x:x[1])
for i in range(k):
  if i < len(result):
    print(result[i][0])
  else:
    break