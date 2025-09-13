"""
    A palindrome number is a number that remains the same when reversed
"""
original_number = 1221
number = original_number
palindrome = 0

while number > 0:
    digit = number % 10
    palindrome = (palindrome * 10) + digit
    number = number // 10
    

# Check if the number is palindrome. We are checking with original_number, not with number, because when the while loop ends, 
# the variable number becomes 0.
if original_number == palindrome:
    print("This is palindrome")
else:
    print("This is not palindrome")

