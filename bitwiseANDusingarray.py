N=int(input())
result=1
n=[int(i) for i in input().split()[:N]]
for i in range(0,len(n)):
  result=result&n[i]
print(result)
