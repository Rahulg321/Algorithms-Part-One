
def fib(n):
    memo = {
        0:0,
        1:1,
    }
    
    return calc_fib(n,memo)
    

def calc_fib(n,memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = calc_fib(n-1,memo) + calc_fib(n-2,memo)
    
    return memo[n]

print(fib(100))
