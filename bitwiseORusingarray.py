N=int(input())
sum=0
n=[int(i) for i in input().split()[:N]]
for i in range(0,len(n)):
  sum=sum|n[i]
print(sum)
