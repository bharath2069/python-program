import math
a,b=map(int,input().split())
if b==0:
  print(a)
else:
  print(math.gcd(a,b))
