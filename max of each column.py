#max of each column matrix
n=int(input())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(0,n):
    maxx=a[0][i]
    for j in range(0,n):
        if a[i][j]>maxx:
            maxx=a[i][j]
    print(maxx,end='')
