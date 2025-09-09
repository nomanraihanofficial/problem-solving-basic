"""
    Imagine you are 3 friends. You all got marks in math.
    One got 70, another got 60, and the third friend got 80.
    You have to write code to find out who got the maximum number.
"""

a = 70
b = 60
c = 80

if a > b and a > c:             # each variable is compared with both 
    print("a is maximum")
elif b > a and b > c:           # each variable is compared with both 
    print("b is maximum")
else:                          
    print("c is maximum")
