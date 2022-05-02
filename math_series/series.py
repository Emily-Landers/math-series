def fibonacci(n):
    '''Takes in a number n, return the nth value in the fibonacci series'''

    if n <= 1:
        return n 
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))
    
def lucas(n):
    '''Takes in a number n, that returns the nth value in the lucas numbers '''

    if (n == 0):
        return 2
        
    if (n == 1):
        return 1
        
    else:
        return lucas(n - 1) + lucas(n - 2);

def sum_series(n, first = 0, second = 1):
    '''Takes in a number n, if n is zero returns zero, if its one, returns one, and then will determine the first two values for the series to be produced.'''

    if n == 0:
        return first
    if n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)
    
    