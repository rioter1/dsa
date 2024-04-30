'''ef gridtraveller(m,n, memo={}):
    gridtraveller(n,m) == gridtraveller(m,n)
    if m==1 and n==1:
        return 1
    elif m==0 or n==0:
        return 0
    else:
        return gridtraveller(m-1,n)+gridtraveller(m,n-1)
    

print(gridtraveller(3,3,{}))'''

def gridtraveller(m,n, memo={}):
    
    if (n,m) in memo:
        return memo[(n,m)]
    if (m,n) in memo:
        return memo(m,n)
    
    if m==1 and n==1:
        return 1
    elif m==0 or n==0:
        return 0
    
    
    x = gridtraveller(m-1,n, memo)+gridtraveller(m,n-1, memo)
    memo[(m,n)] = x
    memo[(n,m)] = x
    return x

print(gridtraveller(18,18,{}))