"""
    here are two ways to sum natural numbers:

    1. Sum all natural numbers one by one                  - Big O(n)
    2. Use the mathematical formula to sum natural numbers - Big O(1)

"""

# Method 1: Loop method - O(n)
N = 5
total_sum = 0
for i in range(1, N+1):
    total_sum += i
print(f"Sum of the first {N} natural numbers using loop: {total_sum}")

# Method 2: Mathematical formula - O(1)
number = 5
sum_of_numbers = number * (number + 1) #// 2
print(f"Sum of the first {number} natural numbers using formula: {sum_of_numbers}")