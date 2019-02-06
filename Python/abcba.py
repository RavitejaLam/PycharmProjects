n=int(input())
N=n
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[:n]+a[n-2::-1])
n-=1
while n:
    print(a[:n]+" "*(2*(N-n)-1)+a[n-1::-1])
    n-=1