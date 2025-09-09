"""
    Swapping two numbers is like exchanging the positions of two different things. 
    For example, if you have salt and sugar in separate cups, and you want to swap them, you would 
    exchange the contents of the two cups

"""


a = 10
b = 5

print("Before swapping:", "a =", a, "b =", b)

a = a + b  # a now becomes 15
b = a - b  # b becomes 10 (original value of a)
a = a - b  # a becomes 5  (original value of b)

print("After swapping:", "a =", a, "b =", b)