def fib(n):
    if n<= 2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))
# print(fib(50))
# fib with memoization
def fib_2(n,memo):
    if memo[n] is not  None:
        return memo[n]
    if n==1 or n==2:
        result=1
    else:
        result=fib_2(n-1,memo)+fib_2(n-2,memo)

    memo[n]=result
    return result   
def fib_memo(n):
    memo=[None] *(n+1)
    return fib_2(n,memo)
print(fib_memo(50))