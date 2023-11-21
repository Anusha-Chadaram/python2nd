#even odd separation
n=int(input())
#l=list(map(int,input().split()))
even=[]
odd=[]
for i in range(1,n):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
#res=even+odd
for i in odd:
    print(i,end=' ')
