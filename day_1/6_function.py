# We use functions to avoid repeating code.
# There are two steps to using functions:
# 1. Define the function
# 2. Call the function

# Function definition
# We use the 'def' keyword to define a function.
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

# Function call
x = -1
print(sign(x))

x = 0
print(sign(x))

x = 1
print(sign(x))


# Function definition
def greet(name, loud=False):
    if loud:
        print('HELLO,', name.upper())
    else:
        print('Hello,', name)

# Function call
# Calling the 'greet' function with only the required 'name' argument.
greet('BIO63 Students')
# Calling the 'greet' function with both 'name' and 'loud' keyword arguments.
greet('BIO63 Students', loud=True)
