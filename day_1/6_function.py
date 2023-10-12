# Function definition
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
greet('BIO63 Students')
greet('BIO63 Students', loud=True)
