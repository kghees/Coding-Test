def inorder(x):
  if x <= n:
    inorder(x*2)
    print(tree[x],end='')
    inorder(x*2+1)
for t in range(1,11):
  n = int(input())
  tree = [[0] for _ in range(n+1)]
  for i in range(n):
    a = input().split()
    tree[int(a[0])] = a[1]
  print(f'#{t}',end=' ')
  inorder(1)
  print()