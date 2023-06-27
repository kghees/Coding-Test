import sys
input = sys.stdin.readline
n = int(input())
s1 = list(map(int,input().split()))
m = int(input())
s2 = list(map(int,input().split()))
dic = {}

for i in s1:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for i in s2:
  if i in dic:
    print(dic[i],end=' ')
  else:
    print(0,end=' ')