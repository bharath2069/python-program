
num=int(input())
count=0
for i in range(1,num//2):
  if num%i==0:
    count=count+1
if count>1:
  print("yes")
else:
  print("no")
