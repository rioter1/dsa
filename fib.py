'''def fib(n):
    if n== 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

print(fib(5))'''
#memoization
def fib(n, memo={}):
    if n== 0:
        return 1
    elif n == 1:
        return 1
    
    memo[n]= fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(40))