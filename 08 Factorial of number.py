"""
    Factorial of a number is a mathematical function that multiplies the number by every positive 
    whole number less than it, down to 1.

    For example:  
    5! = 5 x 4 x 3 x 2 x 1 = 120

    In the code below, we multiply all numbers from 1 up to the value of n. The output is the 
    factorial of n will be same either you multiply from n to 1 or 1 to n.
"""


n = 5

# "The initial value of factorial should be set to 1. "
# "Remember, don't set the factorial's value to 0 because multiplying any number by 0 will result in 0."
factorial = 1                  

for i in range(1, n + 1):
    factorial = factorial * i

print(f"The factorial of {n} is: {factorial}")