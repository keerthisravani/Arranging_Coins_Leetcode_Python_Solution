def arrangeCoins(n):
    count=0
    if n==0:
        return 0
    i=0
    while count<=n:
        i+=1
        count=count+i
    return i-1
n=5
print(arrangeCoins(n))
    