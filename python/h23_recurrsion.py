#factoral
def factorial(n):
    if n==0 or n==1:
        return 1
    fact=n * factorial(n-1)
    return fact

print(factorial(51))