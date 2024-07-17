a = float(input('1st Number'))
x = input('op')
b = float(input('2nd Number'))
def add(a,b):
    if x == '+':
        return (a+b)
    elif x == '-':
        return (a - b)
    elif x == '*':
        return (a * b)
    elif x == '/':
        return (a / b)
        return x
print(add(a,b))
