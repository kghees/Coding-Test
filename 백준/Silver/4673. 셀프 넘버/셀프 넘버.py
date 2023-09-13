num = set(range(1, 10001))
arr = set()

for i in num:				
    for n in str(i):	 
     i += int(n)	
    arr.add(i)

s = num - arr
s = sorted(s)
for i in s:
  print(i)