n = eval(input('Enter a number to find its factorial.'))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))
