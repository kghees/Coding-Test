import sys
input = sys.stdin.readline
a, b = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
xrr = list(set(arr) ^ set(brr))
print(len(xrr))