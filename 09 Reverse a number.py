
number = 1234
reverse = 0

while number > 0:
    digit = number % 10          # Get the last digit of the number
    reverse = (reverse * 10) + digit  # Shift the reverse number left by one digit and add the new digit
    number = number // 10        # Remove the last digit from the original number (integer division)

print(reverse)