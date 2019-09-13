N,K=map(int,input().split())
n=[int(i) for i in input().split()[:N]]
count=0
for i in range(0,len(n)):
  if n[i]==K:
    count=count+1
if count>1:
  print(count-1)
elif count==1:
  print(0)
else:
  print(-1)
  
